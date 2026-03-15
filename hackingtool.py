#!/usr/bin/env python3
import sys

# ── Python version guard (must be before any other local import) ───────────────
if sys.version_info < (3, 10):
    print(
        f"[ERROR] Python 3.10 or newer is required.\n"
        f"You are running Python {sys.version_info.major}.{sys.version_info.minor}.\n"
        f"Upgrade with: sudo apt install python3.10"
    )
    sys.exit(1)

import os
import webbrowser
from itertools import zip_longest

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt, Confirm
from rich.align import Align
from rich.text import Text
from rich import box
from rich.rule import Rule
from rich.columns import Columns

from core import HackingToolsCollection, clear_screen, console
from constants import VERSION_DISPLAY, REPO_WEB_URL
from config import get_tools_dir
from tools.anonsurf import AnonSurfTools
from tools.ddos import DDOSTools
from tools.exploit_frameworks import ExploitFrameworkTools
from tools.forensics import ForensicTools
from tools.information_gathering import InformationGatheringTools
from tools.other_tools import OtherTools
from tools.payload_creator import PayloadCreatorTools
from tools.phishing_attack import PhishingAttackTools
from tools.post_exploitation import PostExploitationTools
from tools.remote_administration import RemoteAdministrationTools
from tools.reverse_engineering import ReverseEngineeringTools
from tools.sql_injection import SqlInjectionTools
from tools.steganography import SteganographyTools
from tools.tool_manager import ToolManager
from tools.web_attack import WebAttackTools
from tools.wireless_attack import WirelessAttackTools
from tools.wordlist_generator import WordlistGeneratorTools
from tools.xss_attack import XSSAttackTools

# ── Tool registry ──────────────────────────────────────────────────────────────

# (full_title, icon, menu_label)
# menu_label is the concise name shown in the 2-column main menu grid.
# full_title is shown when entering the category.
tool_definitions = [
    ("Anonymously Hiding Tools",           "🛡 ", "Anonymously Hiding"),
    ("Information gathering tools",        "🔍",  "Information Gathering"),
    ("Wordlist Generator",                 "📚",  "Wordlist Generator"),
    ("Wireless attack tools",              "📶",  "Wireless Attack"),
    ("SQL Injection Tools",                "🧩",  "SQL Injection"),
    ("Phishing attack tools",              "🎣",  "Phishing Attack"),
    ("Web Attack tools",                   "🌐",  "Web Attack"),
    ("Post exploitation tools",            "🔧",  "Post Exploitation"),
    ("Forensic tools",                     "🕵 ", "Forensics"),
    ("Payload creation tools",             "📦",  "Payload Creation"),
    ("Exploit framework",                  "🧰",  "Exploit Framework"),
    ("Reverse engineering tools",          "🔁",  "Reverse Engineering"),
    ("DDOS Attack Tools",                  "⚡",  "DDOS Attack"),
    ("Remote Administrator Tools (RAT)",   "🖥 ", "Remote Admin (RAT)"),
    ("XSS Attack Tools",                   "💥",  "XSS Attack"),
    ("Steganography tools",                "🖼 ", "Steganography"),
    ("Other tools",                        "✨",  "Other Tools"),
    ("Update or Uninstall | Hackingtool",  "♻ ",  "Update / Uninstall"),
]

all_tools = [
    AnonSurfTools(),
    InformationGatheringTools(),
    WordlistGeneratorTools(),
    WirelessAttackTools(),
    SqlInjectionTools(),
    PhishingAttackTools(),
    WebAttackTools(),
    PostExploitationTools(),
    ForensicTools(),
    PayloadCreatorTools(),
    ExploitFrameworkTools(),
    ReverseEngineeringTools(),
    DDOSTools(),
    RemoteAdministrationTools(),
    XSSAttackTools(),
    SteganographyTools(),
    OtherTools(),
    ToolManager(),
]

# Used by generate_readme.py
class AllTools(HackingToolsCollection):
    TITLE = "All tools"
    TOOLS = all_tools


# ── Help overlay ───────────────────────────────────────────────────────────────

def show_help():
    console.print(Panel(
        Text.assemble(
            ("  Main menu\n", "bold white"),
            ("  ─────────────────────────────────────\n", "dim"),
            ("  1–17   ", "bold cyan"), ("open a category\n", "white"),
            ("  18     ", "bold cyan"), ("Update / Uninstall hackingtool\n", "white"),
            ("  ?      ", "bold cyan"), ("show this help\n", "white"),
            ("  q      ", "bold cyan"), ("quit hackingtool\n\n", "white"),
            ("  Inside a category\n", "bold white"),
            ("  ─────────────────────────────────────\n", "dim"),
            ("  1–N    ", "bold cyan"), ("select a tool\n", "white"),
            ("  99     ", "bold cyan"), ("back to main menu\n", "white"),
            ("  98     ", "bold cyan"), ("open project page (if available)\n\n", "white"),
            ("  Inside a tool\n", "bold white"),
            ("  ─────────────────────────────────────\n", "dim"),
            ("  1      ", "bold cyan"), ("install tool\n", "white"),
            ("  2      ", "bold cyan"), ("run tool\n", "white"),
            ("  99     ", "bold cyan"), ("back to category\n", "white"),
        ),
        title="[bold magenta] ? Quick Help [/bold magenta]",
        border_style="magenta",
        box=box.ROUNDED,
        padding=(0, 2),
    ))
    Prompt.ask("[dim]Press Enter to return[/dim]", default="")


# ── Main menu renderer ─────────────────────────────────────────────────────────

def build_menu():
    clear_screen()

    # ── Compact header ──
    console.print(Panel(
        Text.assemble(
            ("\n    ⚔   H A C K I N G  T O O L\n\n", "bold magenta"),
            ("    All-in-One Security Research Framework", "white"),
            ("   ·   ", "dim"),
            (VERSION_DISPLAY, "bold green"),
            ("\n    ", ""),
            (REPO_WEB_URL, "dim cyan"),
            ("\n\n    ", ""),
            ("For authorized security testing only\n", "dim red"),
        ),
        box=box.HEAVY,
        border_style="magenta",
        padding=(0, 2),
    ))

    # ── 2-column category grid ──
    # Items 1-17 in two columns, item 18 (ToolManager) shown separately
    categories = tool_definitions[:-1]   # 17 items
    update_def = tool_definitions[-1]    # ToolManager

    mid = (len(categories) + 1) // 2    # 9  (left), 8 (right)
    left  = list(enumerate(categories[:mid],  start=1))
    right = list(enumerate(categories[mid:],  start=mid + 1))

    grid = Table.grid(padding=(0, 1), expand=True)
    grid.add_column("ln", justify="right", style="bold magenta", width=5)
    grid.add_column("li", width=3)
    grid.add_column("lt", style="magenta", ratio=1, no_wrap=True)
    grid.add_column("gap", width=3)
    grid.add_column("rn", justify="right", style="bold magenta", width=5)
    grid.add_column("ri", width=3)
    grid.add_column("rt", style="magenta", ratio=1, no_wrap=True)

    for (li, (_, lic, ll)), r in zip_longest(left, right, fillvalue=None):
        if r:
            ri, (_, ric, rl) = r
            grid.add_row(str(li), lic, ll, "", str(ri), ric, rl)
        else:
            grid.add_row(str(li), lic, ll, "", "", "", "")

    console.print(Panel(
        grid,
        title="[bold magenta] Select a Category [/bold magenta]",
        border_style="bright_magenta",
        box=box.ROUNDED,
        padding=(0, 1),
    ))

    # ── ToolManager row ──
    console.print(
        f"  [bold magenta]  18[/bold magenta]  {update_def[1]}  "
        f"[magenta]{update_def[2]}[/magenta]"
    )

    # ── Hint bar ──
    console.print(Rule(style="dim magenta"))
    console.print(
        "  [dim]Enter number to open  ·  "
        "[bold cyan]?[/bold cyan] help  ·  "
        "[bold cyan]q[/bold cyan] quit[/dim]\n"
    )


# ── Main interaction loop ──────────────────────────────────────────────────────

def interact_menu():
    while True:
        try:
            build_menu()
            raw = Prompt.ask("[bold magenta]>[/bold magenta]", default="").strip().lower()

            if not raw:
                continue

            if raw in ("?", "help"):
                show_help()
                continue

            if raw in ("q", "quit", "exit"):
                console.print(Panel(
                    "[bold white on magenta]  Goodbye — Come Back Safely  [/bold white on magenta]",
                    box=box.HEAVY, border_style="magenta",
                ))
                break

            try:
                choice = int(raw)
            except ValueError:
                console.print("[red]⚠  Invalid input — enter a number, ? for help, or q to quit.[/red]")
                Prompt.ask("[dim]Press Enter to continue[/dim]", default="")
                continue

            if 1 <= choice <= len(all_tools):
                title, icon, _ = tool_definitions[choice - 1]
                console.print(Panel(
                    f"[bold magenta]{icon}  {title}[/bold magenta]",
                    border_style="magenta", box=box.ROUNDED,
                ))
                try:
                    all_tools[choice - 1].show_options()
                except Exception as e:
                    console.print(Panel(
                        f"[red]Error while opening {title}[/red]\n{e}",
                        border_style="red",
                    ))
                    Prompt.ask("[dim]Press Enter to return to main menu[/dim]", default="")
            else:
                console.print(f"[red]⚠  Choose 1–{len(all_tools)}, ? for help, or q to quit.[/red]")
                Prompt.ask("[dim]Press Enter to continue[/dim]", default="")

        except KeyboardInterrupt:
            console.print("\n[bold red]Interrupted — exiting[/bold red]")
            break


# ── Entry point ────────────────────────────────────────────────────────────────

def main():
    try:
        from os_detect import CURRENT_OS

        if CURRENT_OS.system == "windows":
            console.print(Panel("[bold red]Please run this tool on Linux or macOS.[/bold red]"))
            if Confirm.ask("Open guidance link in your browser?", default=True):
                webbrowser.open_new_tab(f"{REPO_WEB_URL}#windows")
            return

        if CURRENT_OS.system not in ("linux", "macos"):
            console.print(f"[yellow]Unsupported OS: {CURRENT_OS.system}. Proceeding anyway...[/yellow]")

        get_tools_dir()   # ensures ~/.hackingtool/tools/ exists
        interact_menu()

    except KeyboardInterrupt:
        console.print("\n[bold red]Exiting...[/bold red]")


if __name__ == "__main__":
    main()
