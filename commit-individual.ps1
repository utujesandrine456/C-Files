# Simple script to commit each file individually
# This will only commit files that have changes

Write-Host "Finding files with changes..." -ForegroundColor Green

# Get all files that have changes (modified, added, or untracked)
$files = @()

# Modified files
$modified = git diff --name-only
if ($modified) { $files += $modified }

# Staged files  
$staged = git diff --cached --name-only
if ($staged) { $files += $staged }

# Untracked files
$untracked = git ls-files --others --exclude-standard
if ($untracked) { $files += $untracked }

# Remove duplicates and empty entries
$files = $files | Where-Object { $_ -and $_.Trim() -ne "" } | Sort-Object | Get-Unique

if ($files.Count -eq 0) {
    Write-Host "No files to commit. Make some changes first!" -ForegroundColor Yellow
    exit
}

Write-Host "Files to commit:" -ForegroundColor Cyan
$files | ForEach-Object { Write-Host "  - $_" -ForegroundColor White }

Write-Host ""
$proceed = Read-Host "Commit each file separately? (y/n)"

if ($proceed -eq 'y' -or $proceed -eq 'Y' -or $proceed -eq 'yes') {
    $count = 1
    foreach ($file in $files) {
        Write-Host "[$count/$($files.Count)] Committing: $file" -ForegroundColor Blue
        
        git add $file
        git commit -m "Add/Update: $file"
        
        if ($LASTEXITCODE -eq 0) {
            Write-Host "✓ Successfully committed: $file" -ForegroundColor Green
        } else {
            Write-Host "✗ Failed to commit: $file" -ForegroundColor Red
        }
        
        $count++
    }
    
    Write-Host "`nDone! All files committed individually." -ForegroundColor Green
    Write-Host "View commits: git log --oneline" -ForegroundColor Cyan
} else {
    Write-Host "Cancelled." -ForegroundColor Yellow
}