import sys
import configparser
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich import box
from utils.logger import setup_logger

from core import scanner, recon, exploit, creds, payloads, c2

console = Console()
config = configparser.ConfigParser()
config.read("config.ini")
log = setup_logger(config.get("DEFAULT", "log_level"))

def show_banner():
    banner = Panel.fit(
        "[bold cyan]Advanced Offensive Multi-Tool (v1.0)[/bold cyan]\n[dim]Author: nerdblud | Ctrl+C to quit[/dim]",
        title="[bold white]AOMT[/bold white]",
        border_style="bright_magenta"
    )
    console.print(banner)

def show_menu():
    table = Table(box=box.SIMPLE_HEAVY)
    table.add_column("Option", style="cyan", justify="center")
    table.add_column("Module", style="green")

    table.add_row("[1]", "Reconnaissance")
    table.add_row("[2]", "Port & Service Scanning")
    table.add_row("[3]", "Exploitation")
    table.add_row("[4]", "Credential Attacks")
    table.add_row("[5]", "Payload Generation")
    table.add_row("[6]", "Command & Control (C2)")
    table.add_row("[7]", "SSH Operations")
    table.add_row("[0]", "Exit")

    console.print(table)

def main_menu():
    show_banner()

    while True:
        show_menu()
        try:
            choice = console.input("[bold yellow]> Choose an option:[/bold yellow] ")

            if choice == "1":
                target = console.input("[bold cyan]Target (domain/IP): [/bold cyan]")
                recon.run(target, config)

            elif choice == "2":
                target = console.input("[bold cyan]Target (domain/IP): [/bold cyan]")
                scanner.run(target, config)

            elif choice == "3":
                target = console.input("[bold cyan]Target (URL): [/bold cyan]")
                ex_type = console.input("[bold cyan]Exploit Type (sqli/xss): [/bold cyan]")
                exploit.run(target, ex_type, config)

            elif choice == "4":
                target = console.input("[bold cyan]Target (IP/Login URL): [/bold cyan]")
                creds.run(target, config)

            elif choice == "5":
                reverse_ip = console.input("[bold cyan]Your IP for reverse shell: [/bold cyan]")
                payloads.run(reverse_ip, config)

            elif choice == "6":
                port = int(console.input("[bold cyan]C2 Server Port: [/bold cyan]"))
                c2.run(port, config)

            elif choice == "7":
                console.print("[bold red]SSH Operations are under development.[/bold red]")

            elif choice == "0":
                console.print("[bold green]Exiting AOMT. Stay stealthy.[/bold green]")
                sys.exit(0)

            else:
                console.print("[red]Invalid selection. Try again.[/red]")

        except KeyboardInterrupt:
            console.print("\n[bold red]Interrupted by user. Exiting...[/bold red]")
            sys.exit(0)

if __name__ == "__main__":
    main_menu()

    console.print("[bold red]Exiting AOMT. Stay stealthy.[/bold red]")