import speedtest

st = speedtest.Speedtest()

#Download speed
download = st.download()
#Upload speed
upload = st.upload()

#Result
print("Your Download speed is: ", download)
print("Your Upload speed is: ", upload)

#Fetch the ping
st.get_servers([])
ping = st.results.ping

#Display ping result
print("Your ping is: ", ping)