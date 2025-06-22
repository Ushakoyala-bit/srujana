import demoji

demoji.download_codes()



text = "🎶🐾🧿🧩🎵🎼⏳🌻🍀🍃🥀🍂"
emojis_found = demoji.findall(text)

print(emojis_found)
