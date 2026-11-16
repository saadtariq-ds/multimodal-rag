from __future__ import annotations

import os
import sys
from pathlib import Path
from typing import Any, Sequence
from uuid import NAMESPACE_URL, uuid5
from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore, RetrievalMode
from langchain_text_splitters import RecursiveCharacterTextSplitter
from qdrant_client import QdrantClient, models
from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

load_dotenv(PROJECT_ROOT / ".env")

from exception.custom_exception import DocumentPortalException
from logger.custom_logger import CustomLogger
from src.parsing import ComplexPDFParser

logger = CustomLogger().get_logger(__name__)


class MultiModalDocumentIngestion:
    def __init__(self, document_path: str):
        pass

    def ingest(self):
        pass

    def _ensure_collection(self):
        pass

    def _document_id(self):
        pass

    def _point_id(self):
        pass

    def _split(self):
        pass

    def prepare_document(self):
        pass

    def _delete_existing_document(self):
        pass

    def ingest_document(self):
        pass

    def ingest_pdf(self):
        pass

    def get_vector_store(self):
        pass