# build_handbook.py
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Parent Defense Ontario - CYFSA Handbook</title>
    <style>
        :root { --primary: #2c3e50; --accent: #e74c3c; --bg: #f4f7f6; }
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; line-height: 1.6; color: #333; background: var(--bg); margin: 0; padding: 20px; }
        .container { max-width: 800px; margin: auto; background: white; padding: 40px; border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); }
        h1, h2 { color: var(--primary); border-bottom: 2px solid var(--primary); padding-bottom: 10px; }
        .checklist-item { display: flex; align-items: flex-start; margin: 15px 0; padding: 10px; background: #fff; border-left: 4px solid var(--accent); }
        input[type="checkbox"] { margin-right: 15px; transform: scale(1.5); }
        textarea { width: 100%; height: 200px; padding: 15px; border: 1px solid #ddd; border-radius: 4px; font-size: 16px; margin-top: 20px; }
        .btn-group { margin-top: 30px; display: flex; gap: 10px; }
        button { padding: 10px 20px; border: none; border-radius: 4px; cursor: pointer; font-weight: bold; }
        .btn-save { background: var(--primary); color: white; }
        .btn-export { background: #27ae60; color: white; }
    </style>
</head>
<body>
<div class="container">
    <h1>Parent Defense Ontario</h1>
    <p><strong>Strict Privacy:</strong> Your data is stored locally in your browser and never uploaded.</p>
    
    <h2>5-Day Statutory Checklist</h2>
    <div id="checklist">
        <div class="checklist-item"><input type="checkbox" id="c1"> <label>Document apprehension (Time, Location, Names of Workers)</label></div>
        <div class="checklist-item"><input type="checkbox" id="c2"> <label>Identify "Kith and Kin" placements (Relative options)</label></div>
        <div class="checklist-item"><input type="checkbox" id="c3"> <label>Contact Legal Aid Ontario (1-800-668-8258)</label></div>
        <div class="checklist-item"><input type="checkbox" id="c4"> <label>Demand "Running Records" from CAS in writing</label></div>
    </div>

    <h2>Personal Case Notes & Timeline</h2>
    <textarea id="caseNotes" placeholder="Write interactions here..."></textarea>

    <div class="btn-group">
        <button class="btn-save" onclick="saveData()">Save Progress</button>
        <button class="btn-export" onclick="window.print()">Export to PDF</button>
    </div>
</div>
<script>
    window.onload = function() {
        const saved = localStorage.getItem('parent_notes');
        if (saved) document.getElementById('caseNotes').value = saved;
        document.querySelectorAll('input[type="checkbox"]').forEach(cb => {
            cb.checked = localStorage.getItem(cb.id) === 'true';
            cb.addEventListener('change', () => localStorage.setItem(cb.id, cb.checked));
        });
    };
    function saveData() {
        localStorage.setItem('parent_notes', document.getElementById('caseNotes').value);
        alert("Progress saved locally.");
    }
</script>
</body>
</html>
"""

with open("ParentDefense.html", "w") as f:
    f.write(html_content)

print("File 'ParentDefense.html' created successfully. Open it in your browser to begin.")
