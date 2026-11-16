from __future__ import annotations

import os
import sys
from pathlib import Path
from typing import Any, Iterable
from langchain_core.documents import Document
from langchain_core.vectorstores import VectorStoreRetriever
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore, RetrievalMode
from qdrant_client import QdrantClient, models
from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

load_dotenv(PROJECT_ROOT / ".env")

from exception.custom_exception import DocumentPortalException
from logger.custom_logger import CustomLogger

logger = CustomLogger().get_logger(__name__)


class MultiModalRetriever:
    def __init__(self):
        pass

    def retrieve(self):
        pass

    def _validate_collection(self):
        pass

    def _normalize_content_types(self):
        pass

    def build_filter(self):
        pass

    def retrieve(self):
        pass

    def retrieve_with_scores(self):
        pass

    def as_langchain_retriever(self):
        pass

    def format_results(self):
        pass

    def collection_status(self):
        pass

