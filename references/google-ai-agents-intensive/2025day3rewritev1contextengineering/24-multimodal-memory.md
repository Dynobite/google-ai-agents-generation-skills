## Multimodal memory

"Multimodal memory" is a crucial concept that describes how an agent handles non-textual information, like images, videos, and audio. The key is to distinguish between the data the memory is derived from (its source ) and the data the memory is stored as (its content ).

Memory from a multimodal source is the most common implementation. The agent can process various data types-text, images, audio-but the memory it creates is a textual insight derived from that source. For example, an agent can process a user's voice memo to create memories. It doesn't store the audio file itself; instead, it transcribes the audio and creates a textual memory like, "User expressed frustration about the recent shipping delay."

Memory with Multimodal Content is a more advanced approach where the memory itself contains non-textual media. The agent doesn't just describe the content; it stores the content directly. For example, a user can upload an image and say "Remember this design for our logo." The agent creates a memory that directly contains the image file, linked to the user's request.

Most contemporary memory managers focus on handling multimodal sources while producing textual content. This is because generating and retrieving unstructured binary data like images or audio for a specific memory requires specialized models, algorithms, and infrastructure. It is far simpler to convert all inputs into a common, searchable format: text.

For example, you can generate memories from multimodal input 16  using Agent Engine Memory Bank. The output memories will be textual insights extracted from the content:

```
Python from google.genai import types client = vertexai.Client(project=..., location=...) response = client.agent_engines.memories.generate( name=agent_engine_name, direct_contents_source={ "events": [ { "content": types.Content( role="user", parts=[ types.Part.from_text( "This is context about the multimodal input." ), Continues next page...
```

```
types.Part.from_bytes( data=CONTENT_AS_BYTES, mime_type=MIME_TYPE ), types.Part.from_uri( file_uri="file/path/to/content", mime_type=MIME_TYPE ) ])}]}, scope={"user_id": user_id} )
```

Snippet 5: Example memory generation API call for Agent Engine Memory Bank

The next section examines the mechanics of memory generation, detailing the two core stages: the extraction of new information from source data, and the subsequent consolidation of that information with the existing memory corpus.
