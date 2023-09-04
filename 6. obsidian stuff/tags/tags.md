### gen
```dataview
list sort(rows.file.link) from "6. obsidian stuff/tags/gen"
group by split(file.folder, "/")[3]
```

### personal
```dataview
list sort(rows.file.link) from "6. obsidian stuff/tags/personal"
group by split(file.folder, "/")[3]
```
