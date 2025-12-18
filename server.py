from flask import Flask, render_template, request, jsonify


app = Flask(__name__)

snippets = []


@app.route("/")
def index():
    return render_template("index.html", snippets=snippets)

@app.route("/add", methods=["POST"])
def add_snippet():
    data = request.get_json()
    new_id = len(snippets)
    snippets.append({
        "id": new_id,
        "language": data.get("language", ""),
        "code": data.get("code", "")
    })
    return jsonify({"status": "ok"})

@app.route("/delete/<int:snippet_id>", methods=["POST"])
def delete_snippet(snippet_id):
    global snippets
    snippets = [s for s in snippets if s["id"] != snippet_id]
    return jsonify({"status": "deleted"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)