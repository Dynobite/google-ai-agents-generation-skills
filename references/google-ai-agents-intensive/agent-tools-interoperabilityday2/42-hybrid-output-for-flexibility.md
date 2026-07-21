## Hybrid Output for Flexibility

Provide both data and UI so consumers can choose:

```
JSON { "data": {"sales": [...]}, "ui": {"version": "v0.9", "updateComponents": {"surfaceId": "main", "components": [...]}}, "ui_available": true }
```

Snippet 7: Hybrid Output Example Schema

API clients ignore the ui field and use data . Human-facing clients render the A2UI message.
