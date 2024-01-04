# Implement paper : "μVulDeePecker: A Deep Learning-BasedSystem for Multiclass Vulnerability Detection"



<a name="readme-top"></a>



[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][contributors-url]
[![Stargazers][stars-shield]][contributors-url]
[![Issues][issues-shield]][contributors-url]
[![MIT License][license-shield]][contributors-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<!-- <div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Best-README-Template</h3>

  <p align="center">
    An awesome README template to jumpstart your projects!
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template">View Demo</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Report Bug</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Request Feature</a>
  </p>
</div> -->



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This project is created to classfication 40 cwe in program c/c++, this project implement base on paper  [μVulDeePecker: A Deep Learning-Based
System for Multiclass Vulnerability Detection](https://github.com/nguyenvuong1309/hotel_booking_client.git)

Architect of my project.
![image](https://github.com/nguyenvuong1309/Do-an-lap-trinh-an-toan/assets/100818110/51a482e7-93a6-45a7-b95a-2cad9c395634)


<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Tensorflow][Tensorflow]][Tensorflow-url]
* [![Numpy][Numpy]][Numpy-url]
* [![Pandas][Pandas]][Pandas-url]
* [![Matplotlib][Matplotlib]][Matplotlib-url]
* [![Keras][Keras]][Keras-url]


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started
### Prerequisites

* python
* tensorflow
* numpy
* pandas
* seaborn

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/nguyenvuong1309/hotel_booking_client.git
   ```
2. Install all the package require.

3. Prepare dataset and train model.
- Download file mvd.txt.zip ( dataset ) and file label2CWE.txt ( label ) from the link https://github.com/muVulDeePecker/muVulDeePecker
- Then run file create_text_dataset.py to create dataset .csv to train model.
- Then run file BLSTM.ipynb to train model.

4. Run deploy web app.
- Run web app using this command.
```s
 streamlit run streamlit-app.py
```
- Then you can paste direct source code c/c++ or upload file and then using model to predict wherether the code have vulnerability or not. If yes, the program can predict which CWE.

![image](https://github.com/nguyenvuong1309/Do-an-lap-trinh-an-toan/assets/100818110/2161f56f-b22d-413d-ad0e-a95b57d84e1d)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- LICENSE -->
## License
Nguyễn Đức Vương


<!-- CONTACT -->
## Contact

Email - 21522809@gm.uit.edu.vn or nguyenducvuong13092003@gmail.com



<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/nguyenvuong1309
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/v%C6%B0%C6%A1ng-nguy%E1%BB%85n-%C4%91%E1%BB%A9c-77aa2824a/
[product-screenshot]: images/screenshot.png



[Tensorflow-url]: https://www.tensorflow.org/
[Tensorflow]: https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white

[Numpy-url]: https://numpy.org/
[Numpy]: https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white

[Pandas-url]: https://pandas.pydata.org/
[Pandas]: https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white

[Matplotlib-url]: https://matplotlib.org/
[Matplotlib]: https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black

[Keras-url]: https://keras.io/
[Keras]: https://img.shields.io/badge/Keras-%23D00000.svg?style=for-the-badge&logo=Keras&logoColor=white
