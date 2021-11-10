<div id="top"></div>

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
<!--   <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a> -->

  <h3 align="center">gcs_basic_functions</h3>

  <p align="center">
    Google storage basic functions
    <br />
<!--     <a href="https://github.com/othneildrew/Best-README-Template"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template">View Demo</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Report Bug</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Request Feature</a> -->
  </p>
</div>


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#roadmap">Roadmap</a></li>
  </ol>
</details>

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

```python
import gcs_basic
gcs_basic.download(bucket_name, blob_path, down_path, project)
gcs_basic.upload(bucket_name, blob_path, local_path, project)
gcs_basic.list_blobs(bucket_name, blob_path, project)
```

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* python python-pip
  ```sh
  sudo apt-get install python3 python-pip
  #or
  sudo pacman -S python python-pip
  ```
* Google cloud SDK for credentials - temporarily
```
wget https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-364.0.0-linux-x86_64.tar.gz
tar -xvf google-cloud-sdk-364.0.0-linux-x86_64.tar.gz
cd google-cloud-sdk-364.0.0-linux-x86_64
bash google-cloud-sdk/install.sh
#open new terminal
gcloud init
gcloud auth application-default login
```
### Installation
1. Clone the repo
   ```sh
   git clone https://github.com/antonio258/gcs_basic_functions.git
   ```
2. Install package
   ```sh
   cd gcs_basic_functions
   pip install .
   ```

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- ROADMAP -->
## Roadmap

- [x] Download one file from storage
- [x] Upload one file to storage
- [x] Download folder from storage
- [x] Upload folder to storage
- [x] list blobs
- [ ] check credentials in library

