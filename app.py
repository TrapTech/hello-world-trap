from flask import Flask, render_template, redirect, url_for, request
import subprocess
import base64

def run_trap_cli(args):
    try:
        cmdline = ["TrapCLI"] + args
        app.logger.info(f"Executing {cmdline}")
        subprocess.run(cmdline)
    except Exception as err:
        app.logger.error("Error executing TrapCLI", err)

app = Flask(__name__)

@app.route("/")
def index():
    return redirect(url_for('step_1_hello_world'))

#
# Step 1 handlers
#
@app.route("/1-hello-world")
def step_1_hello_world():
    return render_template('1-hello-world/index.html')

@app.route("/1-hello-world/notify")
def step_1_notify():
    run_trap_cli([
        "send-incident",
        "-n", "Step 1 - Someone entered the trap!",
        "-d", "A simulated attacker has entered your trap",
        "-s", "Info",
        "-i", f"{request.remote_addr}"
    ])
    return render_template('1-hello-world/notify.html')

#
# Step 2 handlers
#
@app.route("/2-incident", methods=["GET", "POST"])
def step_2_incident():
    render = lambda form: render_template('2-incident/index.html', form_state=form)

    if request.method == "GET":
        return render('start')

    escape = lambda arg: arg.replace(",", "").replace("=", "")

    first_name  = escape(request.form.get("fname"))
    second_name = escape(request.form.get("sname"))
    run_trap_cli([
        "send-incident",
        "-n", "Step 2 - SQL injection was executed!",
        "-d", "A simulated attacker has attempted an SQL injection",
        "-s", "Incident",
        "-i", f"{request.remote_addr}",
        "-c", f"FirstName={first_name},SecondName={second_name}"
    ])
    return render('end')

#
# Step 3 handlers
#
@app.route("/3-bait", methods=["GET", "POST"])
def step_3_bait():
    render = lambda form: render_template('3-bait/index.html', form_state=form)

    if request.method == "GET":
        return render('start')

    def validate_bait(v):
        # A valid bait value is one that is a proper base64 string, and which starts
        # with @dv: when decoded.
        try:
            decoded = base64.b64decode(v)
            return decoded.startswith(b'@dv:')
        except:
            return False

    password = request.form.get("pass")
    if validate_bait(password):
        run_trap_cli([
            "send-incident",
            "-n", "Step 3 - Bait used to enter",
            "-d", "A simulated attacker has used a bait to enter the trap",
            "-s", "Attempt",
            "-i", f"{request.remote_addr}",
            "-b", f"{password}"
        ])
        return render('open')

    return render('invalid')


if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=80)
