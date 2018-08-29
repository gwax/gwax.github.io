import json

from nikola.metadata_extractors import MetaCondition, MetaPriority, MetaSource
from nikola.plugin_categories import MetadataExtractor

class JSONMetadata(MetadataExtractor):
    """Extractor for JSON metadata/posts."""

    name = 'json'
    source = MetaSource.text
    priority = MetaPriority.normal
    conditions = ((MetaCondition.first_line, '{'),)

    def _extract_metadata_from_text(self, source_text):
        return json.loads(source_text)

    def split_metadata_from_text(self, source_text):
        data = json.loads(source_text)
        text = data.pop('text')
        return json.dumps(data), text
