function cd {
  builtin cd "$@"
  if [ -d "venv" ] ; then
    source venv/bin/activate
  fi
}