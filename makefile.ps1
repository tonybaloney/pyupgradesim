param (
  [string]$command = "images"
)


function Start-WebApp {
    Set-Location .\profilersite
    Start-Job -ScriptBlock {
        & python manage.py qcluster >qcluster.log 2>qcluster.err
      }
    python manage.py runserver
}

function New-Images {
    docker build -t benchapp-3.8 --build-arg VERSION=3.8 .
	docker build -t benchapp-3.9 --build-arg VERSION=3.9 .
	docker build -t benchapp-3.10 --build-arg VERSION=3.10 .
	docker build -t benchapp-3.11 --build-arg VERSION=3.11 .
}


if ($command -eq "images") {
  New-Images
} elseif ($command -eq "web") {
  Start-WebApp
} else {
  Write-Host "Invalid command"
}
