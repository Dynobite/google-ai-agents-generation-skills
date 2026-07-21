## Judge the rendered artifact, not the code.

In vibe coding the user judges the output, not the diff. A multimodal model looking at the rendered page catches problems that code-level evaluation misses entirely: layout broken on mobile, contrast too low for accessibility, button states wrong. Pair this with Playwright assertions from Section 5, the judge catches visual and design issues, the assertions catch broken interactivity.

```
Python from google import genai from google.genai import types client = genai.Client(vertexai=True, project="...", location="...") result = client.models.generate_content( model="gemini-3-pro", contents=[ "Score this rendered web app against the spec on layout_match, styling, " "and interactive_correctness (1-5 each). Return JSON.", user_spec, types.Part.from_bytes(data=screenshot_bytes, mime_type="image/png"), ], )
```

Snippet 2: Multimodal evaluation of a rendered web application's layout and interactive correctness.
