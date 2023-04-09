<html>
    <head>
        <title>Learm DOM </title>
        <link rel='stylesheet' type='text/css' media='screen' href='https://cdn.jsdelivr.net/npm/bulma@0.9.3/css/bulma.min.css'>
        <link rel="stylesheet" href="https://pyscript.net/alpha/pyscript.css"/>
        <script defer src="https://pyscript.net/alpha/pyscript.js"></script>
    </head>
    <body>
        <h1>Learn DOM MANIPULATION using pyscript</h1>
        <h2>Simple String Counter using Python</h2>
        <br>
        <p>input text</p>
        <textarea name="input_text" id="input_text" placeholder="Enter your Text.."></textarea>
        <button id="run" type="button" class="button is-primary" pys-onClick="count">count</button>
        <button id="run" type="button" class="button is-danger" pys-onClick="count">clear</button>
        <p>Output From</p>
        <p id='output'></p>
    </body>
    <py-script>
    input_text = Element("input_text")
    op = Element("output")
    def clear(*args,**kwargs):
       input_text.clear()
    def count(*args,**kwargs):
        number = len(input_text.value)
        op.write(number)
    </py-script>
</html>
