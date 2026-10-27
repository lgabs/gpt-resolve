from gpt_resolve.providers.guard import check_tool_use


def check(tool, tool_input, tmp_path):
    exam = tmp_path / "exam" / "prova.pdf"
    exam.parent.mkdir(exist_ok=True)
    exam.touch()
    (tmp_path / "exam" / "gabarito.pdf").touch()
    workdir = tmp_path / "work"
    workdir.mkdir(exist_ok=True)
    return check_tool_use(tool, tool_input, workdir, [str(exam)])


def test_reads_only_exam_files_and_workdir(tmp_path):
    assert check("Read", {"file_path": str(tmp_path / "exam" / "prova.pdf")}, tmp_path) is None
    assert check("Read", {"file_path": str(tmp_path / "work" / "x.py")}, tmp_path) is None
    assert check("Read", {"file_path": str(tmp_path / "exam" / "gabarito.pdf")}, tmp_path)
    assert check("Read", {"file_path": str(tmp_path / "work" / ".." / "exam" / "gabarito.pdf")}, tmp_path)
    assert check("Glob", {"pattern": "*", "path": str(tmp_path / "exam")}, tmp_path)
    assert check("WebFetch", {"url": "https://x"}, tmp_path)


def test_bash_allows_local_python_only(tmp_path):
    assert check("Bash", {"command": "python3 -c 'print(2**10)'"}, tmp_path) is None
    assert check("Bash", {"command": f"cat > {tmp_path}/work/a.py <<'EOF'\nimport math\nEOF"}, tmp_path) is None
    assert check("Bash", {"command": "/usr/bin/python3 chk.py"}, tmp_path) is None
    assert check("Bash", {"command": "python3 -c 'print(a/c + 1/9, m*x/cc+m*math.cos(t))'"}, tmp_path) is None
    assert check("StructuredOutput", {"x": 1}, tmp_path) is None
    assert check("Bash", {"command": "curl https://poliedro.com.br"}, tmp_path)
    assert check("Bash", {"command": "python3 -c 'import urllib.request'"}, tmp_path)
    assert check("Bash", {"command": "ls ~/Downloads"}, tmp_path)
    assert check("Bash", {"command": f"ls {tmp_path}/exam"}, tmp_path)
    assert check("Bash", {"command": "ls ../exam"}, tmp_path)
