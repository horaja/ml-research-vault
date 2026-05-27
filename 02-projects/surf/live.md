---
type: project
project: surf
---

# live

Read-only view of open work. Update status fields or check boxes in the source notes.

## active items
```dataview
TABLE status, file.folder AS folder, file.mtime AS updated
FROM "02-projects/surf"
WHERE status = "planned" OR status = "running" OR status = "blocked" OR status = "speculative"
SORT status ASC, file.mtime DESC
```

## open action items
```dataview
TASK
FROM "05-meetings" OR "01-daily-notes" OR "02-projects/surf"
WHERE !checked
GROUP BY file.link
```
