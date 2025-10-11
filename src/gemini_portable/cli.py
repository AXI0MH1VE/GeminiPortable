# GeminiPortable/src/gemini_portable/cli.py
import click
import sys
import json
from .memory4d import Memory4D

# Initialize the 4D memory system
memory_system = Memory4D()

def deterministic_llm_stub(prompt: str) -> str:
    """
    A deterministic LLM stub for sovereign generative AI.
    Produces predictable output based on specific keywords.
    """
    if "AxiomHive principles" in prompt:
        return (
            "The AxiomHive principles are Determinism (H=0), Sovereignty (Local-First), "
            "Verifiable Integrity, Ethics-by-Default, and Offline-First."
        )
    elif "4D memory" in prompt:
        return "The 4D memory system conceptually organizes information across spatio-temporal axes for advanced recall."
    else:
        return f"Deterministic response to: '{prompt}' (LLM stub)."

@click.group()
def main() -> None:
    """GeminiPortable: Sovereign Generative AI CLI."""
    pass

@main.command("run")
@click.option("--prompt", required=True, help="The prompt for the generative AI.")
@click.option("--store-memory", is_flag=True, help="Store the prompt and response in 4D memory.")
def run_command(prompt: str, store_memory: bool) -> None:
    """Run a generative AI prompt and get a deterministic response."""
    click.echo(f"Processing prompt with GeminiPortable: '{prompt}'")
    response = deterministic_llm_stub(prompt)
    click.echo(f"\nGeminiPortable Response:\n{response}")

    if store_memory:
        # Simulate conceptual 4D coordinates for memory storage
        coordinates = {"time": "current", "space": "local", "context": "user_query"}
        memory_system.store(f"Prompt: {prompt}\nResponse: {response}", coordinates)
        click.echo("\nPrompt and response stored in 4D memory.")

@main.command("recall")
@click.option("--query", required=True, help="Query to recall from 4D memory.")
def recall_command(query: str) -> None:
    """Recall information from the local 4D memory system."""
    recalled_items = memory_system.recall(query)
    if recalled_items:
        click.echo(f"\nRecalled memories for query '{query}':")
        for item in recalled_items:
            click.echo(f"- Content: {item['content'][:100]}...")
            click.echo(f"  Coordinates: {item['coordinates']}")
    else:
        click.echo(f"No memories recalled for query '{query}'.")

@main.command("list-memory")
def list_memory_command() -> None:
    """List all stored memories in the 4D memory system."""
    all_memories = memory_system.get_all_memories()
    if all_memories:
        click.echo("\nAll stored memories:")
        for i, item in enumerate(all_memories):
            click.echo(f"--- Memory {i+1} ---")
            click.echo(f"Content: {item['content']}")
            click.echo(f"Coordinates: {item['coordinates']}")
    else:
        click.echo("No memories currently stored.")

if __name__ == "__main__":
    main()
