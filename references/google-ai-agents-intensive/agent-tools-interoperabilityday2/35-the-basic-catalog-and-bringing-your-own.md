## The Basic Catalog (and Bringing Your Own)

A2UI ships a basic catalog of 18 ready-to-use components for prototyping and demos:

Table 1: A2UI Basic Catalog

| Category    | Components                                                       |
|-------------|------------------------------------------------------------------|
| Layout      | Row, Column, List                                                |
| Display     | Text, Image, Icon, Divider                                       |
| Containers  | Card, Modal, Tabs                                                |
| Media       | Video, AudioPlayer                                               |
| Interactive | Button, TextField, CheckBox, Slider, DateTimeInput, ChoicePicker |

This set was called "standard" in v0.8 and renamed to "basic" in v0.9, a deliberate signal that production frontends should bring their own catalog, mapping their existing components (your design-system buttons, your charts, your maps) to A2UI types. The agent doesn't change; only the renderer's catalog mapping does ( ChoicePicker was MultipleChoice in v0.8.)

Here's what an A2UI message looks like (v0.9 format):

```
JSON { "version": "v0.9", "updateComponents": { "surfaceId": "main", "components": [ {"id": "root", "component": "Column", "children": ["title", "summary", "export"]}, {"id": "title", "component": "Text", "text": "Q4 Sales", "variant": "h1"}, {"id": "summary", "component": "Text", "text": "Revenue grew 12% QoQ"}, {"id": "export", "component": "Button", "child": "export-label", "action": {"event": {"name": "export_csv"}}}, {"id": "export-label", "component": "Text", "text": "Export CSV"} ] } }
```

Snippet 4: Example A2UI message

Components form a flat adjacency list referenced by id, which makes the structure easy for an LLM to generate incrementally and easy for the client to update without re-rendering. A separate createSurface message (not shown) tells the client which id is the root. The client then renders this as a complete, interactive interface: no React code required.
