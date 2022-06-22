echo "Executing setup file"
echo [-] Downloading chromedriver
wget https://chromedriver.storage.googleapis.com/102.0.5005.61/chromedriver_linux64.zip
echo [-] Extracting chromedriver
unzip chromedriver_linux64.zip
echo [-] Moving the binary to /bin/
sudo mv chromedriver /bin
