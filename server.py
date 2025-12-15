from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

snippets = []

@app.route("/")
def index():
    return render_template("index.html", snippets=snippets)

@app.route("/add", methods=["POST"])
def add_snippet():
    data = request.json
    snippets.append({
        "id": len(snippets),
        "code": data["code"],
        "language": data.get("language", None)
    })
    return jsonify(success=True)

@app.route("/delete/<int:snippet_id>", methods=["POST"])
def delete_snippet(snippet_id):
    global snippets
    snippets = [s for s in snippets if s["id"] != snippet_id]
    return jsonify(success=True)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
