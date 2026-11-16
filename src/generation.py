from __future__ import annotations

import base64
import os
import sys
from io import BytesIO
from pathlib import Path
from typing import Any, Iterable
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
from PIL import Image
from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parent.parent

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

load_dotenv(PROJECT_ROOT / ".env")

from exception.custom_exception import DocumentPortalException
from logger.custom_logger import CustomLogger
from prompts.prompt import (
    GENERATION_SMOKE_TEST_QUERY,
    MULTIMODAL_RAG_SYSTEM_PROMPT,
    format_multimodal_rag_user_prompt,
    format_retrieved_image_evidence_prompt,
)
from src.retriever import MultimodalQdrantRetriever


class MultiModalRAGGenerator:
    def __init__(self):
        pass

    def _validate_config(self):
        pass

    def _image_to_data_url(self):
        pass

    def _source_label(self):
        pass

    def _prepare_context(self):
        pass

    def _build_messages(self):
        pass

    def _extract_response_text(self):
        pass

    def _usage_metadata(self):
        pass

    def generate(self):
        pass

    def answer_question(self):
        pass