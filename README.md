This repository contains a lightweight setup to run OWASP Dependency-Track locally using Docker Compose, plus instructions to generate a CycloneDX SBOM from a Python project and upload it to the tracker.

docker-compose.yml — Docker Compose file to run Dependency-Track API and Frontend (embedded DB).

Install CycloneDX Python tool:

pip install cyclonedx-bom


Install the dependency :

pip install -r requirements.txt

Generate SBOM from requirements.txt:

cyclonedx-py requirements -i requirements.txt -o bom.json

Upload the SBOM to Dependency-Track (via API)
Use the API endpoint to post the BOM. Replace <YOUR_API_KEY> with the API key you created earlier.

curl -X POST "http://localhost:8086/api/v1/bom" \
  -H "X-Api-Key: GVYMGTfpq3NBcoI1MbYVRC3MtARWQzDI" \
  -F "project=c68b937d-faf0-4c56-9cbf-213c8139b790" \
  -F "bom=@bom.json"

  If upload succeeds, the API returns a 200/202 response and Dependency-Track will process the BOM and populate the project/components view with dependency details and vulnerability matches
