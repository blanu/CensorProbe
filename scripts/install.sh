if [ ! -e "$HOME/.ssh/id_rsa.pub" ]; then
    echo "Generating SSH key"
    expect -c "
      spawn ssh-keygen -b 2048 -t rsa -f "$HOME/.ssh/id_rsa" -q
      expect \"Enter passphrase (empty for no passphrase):\"
      send \"\r\"
      expect \"Enter same passphrase again:\"
      send \"\r\"
    "
fi

scripts/install-deps.sh
