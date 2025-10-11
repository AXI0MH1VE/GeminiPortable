# GeminiPortable/src/gemini_portable/memory4d.py
import logging
from typing import Dict, Any, List

logger = logging.getLogger(__name__)

class Memory4D:
    def __init__(self):
        self.memory_store: List[Dict[str, Any]] = []
        logger.info("Memory4D system initialized for local-first operation.")

    def store(self, content: str, coordinates: Dict[str, Any]) -> None:
        """Stores a piece of content with associated 4D coordinates (conceptual)."""
        self.memory_store.append({"content": content, "coordinates": coordinates})
        logger.debug(f"Stored: {content[:50]}... at {coordinates}")

    def recall(self, query: str) -> List[Dict[str, Any]]:
        """Recalls relevant memories based on a query (simple keyword match for stub)."""
        recalled_memories = [
            mem for mem in self.memory_store if query.lower() in mem["content"].lower()
        ]
        logger.debug(f"Recalled {len(recalled_memories)} memories for query: {query}")
        return recalled_memories

    def get_all_memories(self) -> List[Dict[str, Any]]:
        """Returns all stored memories."""
        return self.memory_store
