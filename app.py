from flask import Flask, request, jsonify
from tasks import long_running_task
from code_scan import code_scan

# Create a Flask application instance
app = Flask(__name__)

@app.route('/')
def hello_world():
    """Returns a simple greeting when the root URL is accessed."""
    return 'Hello, World!'

@app.route("/generate_yaml_preview", methods=["POST"])
def generate_yaml_preview():
    """Generate YAML workflow preview without triggering scan"""
    try:
        data = request.get_json()
        scanner = code_scan()
        
        # Generate YAML without triggering scan
        yaml_data = scanner.generate_dynamic_yaml(data)
        
        if yaml_data["success"]:
            return jsonify({
                "success": True,
                "yaml_content": yaml_data["yaml_content"],
                "detected_languages": yaml_data["detected_languages"],
                "selected_tools": yaml_data["selected_tools"],
                "project_name": yaml_data["project_name"]
            })
        else:
            return jsonify({
                "success": False,
                "error": yaml_data["error"]
            }), 400
            
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.route("/detect_languages", methods=["POST"])
def detect_languages():
    """Auto-detect languages based on selected tools"""
    try:
        data = request.get_json()
        tools = data.get('tools', [])
        
        scanner = code_scan()
        detected_languages = scanner._detect_languages_from_tools(tools)
        
        return jsonify({
            "success": True,
            "detected_languages": detected_languages,
            "tools": tools
        })
        
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.route("/initiate_scan", methods=["POST"])
def add_workflow():
    print(f'======================= >>>>  START API')
    data = request.get_json()
    # selected = set(data.get("tools", []))
    print(f'======================= >>>>  selected_tools - {type(data)}')
    task = long_running_task.delay(data)
    return jsonify({
        "message": "Scan Initiated",
        "task_id": task.id
    })

@app.route("/result/<task_id>")
def result(task_id):
    task = long_running_task.AsyncResult(task_id)
    return jsonify({
        "task_id": task.id,
        "status": task.status,
        "result": task.result
    })

# Initialize code scanner instance
scanner = code_scan()

@app.route("/workflow/runs", methods=["GET"])
def get_workflow_runs():
    """Get recent workflow runs"""
    limit = request.args.get('limit', 10, type=int)
    result = scanner.get_workflow_runs(limit)
    return jsonify(result)

@app.route("/workflow/run/<run_id>", methods=["GET"])
def get_workflow_run_details(run_id):
    """Get detailed information about a specific workflow run"""
    result = scanner.get_workflow_run_details(run_id)
    return jsonify(result)

@app.route("/workflow/run/<run_id>/jobs", methods=["GET"])
def get_workflow_jobs(run_id):
    """Get jobs for a specific workflow run"""
    result = scanner.get_workflow_jobs(run_id)
    return jsonify(result)

@app.route("/workflow/artifacts", methods=["GET"])
def get_workflow_artifacts():
    """Get all recent artifacts or artifacts for a specific run"""
    run_id = request.args.get('run_id')
    result = scanner.get_workflow_artifacts(run_id)
    return jsonify(result)

@app.route("/workflow/run/<run_id>/logs/<job_id>", methods=["GET"])
def get_workflow_logs(run_id, job_id):
    """Get logs for a specific job in a workflow run"""
    result = scanner.get_workflow_logs(run_id, job_id)
    return jsonify(result)

@app.route("/workflow/summary/<run_id>", methods=["GET"])
def get_scan_summary(run_id):
    """Get a comprehensive summary of a scan run"""
    result = scanner.get_scan_summary(run_id)
    return jsonify(result)

@app.route("/tools/available", methods=["GET"])
def get_available_tools():
    """Get list of all available scanning tools"""
    result = scanner.get_available_tools()
    return jsonify(result)

@app.route("/workflow/severity/<run_id>", methods=["GET"])
def get_severity_wise_results(run_id):
    """Get scan results categorized by severity for each tool"""
    result = scanner.get_severity_wise_results(run_id)
    return jsonify(result)

@app.route("/api/scan-results", methods=["POST"])
def receive_scan_results():
    """Receive severity-wise scan results from GitHub Actions workflow"""
    data = request.get_json()
    
    # Extract severity results from the data
    severity_results = data.get('severity_results', {})
    
    # Store or process results as needed
    print(f"Received scan results: {data}")
    print(f"Severity results: {severity_results}")
    
    # You can store in database, file, or process further
    return jsonify({
        "success": True,
        "message": "Scan results received successfully",
        "severity_results": severity_results,
        "run_id": data.get('run_id'),
        "repository": data.get('repository'),
        "branch": data.get('branch')
    })

@app.route("/tools/validate", methods=["POST"])
def validate_tools():
    """Validate if tools are supported"""
    data = request.get_json()
    tools = data.get('tools', [])
    result = scanner.validate_tools(tools)
    return jsonify(result)

if __name__ == '__main__':
    # Run the application (this is only for the development server)
    app.run(debug=True)