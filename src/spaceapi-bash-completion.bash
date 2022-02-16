#/usr/bin/env bash
_spaceapi_completions()
{
  if [ "${#COMP_WORDS[@]}" != "2" ]; then
    return
  fi

  OPTS=$(spaceapi api.getApiCallList 2>/dev/null | grep '^\s*"\w*\.\w*.*: {$' | sed 's/\s*"\([a-zA-Z\.]*\).*{$/\1/')
  COMPREPLY=($(compgen -W "$OPTS" -- "${COMP_WORDS[1]}"))
}

complete -F _spaceapi_completions spaceapi


