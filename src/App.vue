<template>
  <div class="container">
    <title>Leon Bos</title>
    <link
      rel="stylesheet"
      href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css"
    />
    <section id="home" class="home">
      <div id="home" class="home">
        <p class="introduction">
          Hello, my name is <span class="name">Leon Bos</span><br />
          I am a Software Engineering Student
        </p>
        <div class="nav">
          <button @click="scrollToNextPage('about')">About Me</button>
          <button @click="scrollToNextPage('contact')">Contact</button>
        </div>
      </div>
    </section>

    <section id="about">
      <div class="me">
        <img src="./assets/me.png" alt="Leon Bos" class="about-image" />
      </div>
      <div class="about" id="about">
        <div class="title">About</div>

        <div class="about-text">
          My name is Leon Bos and I'm a 21 year old Sofware Engineering student
          at the Hanzehogeschool Groningen.<br />

          I am a hard working and motivated student who is always looking for
          new challenges. <br />

          Currently I am working part time as a junior developer. In February I
          will start my internship at
          <a href="https://www.bencom.nl/">Bencom Group</a>.<br />
          <br />

          If you want to know more about me, feel free to
          <span class="contact-me" @click="scrollToContact()">contact me</span
          >.<br />
          <br />

          I have experience with the following technologies:<br />
          <br />
        </div>

        <!--loop over skills, skills is a key value with skillname: skillpercentage -->

        <div class="skill">
          <div
            class="bar"
            v-for="(skill, skillName) in skills"
            :key="skillName"
          >
            <div :id="skillName" class="fill" :style="{ width: skill + '%' }">
              <div class="tag language">{{ skillName }}</div>
            </div>
          </div>
        </div>

        <!-- <div class="skill">
          <div class="bar">
            <div class="fill" style="width: 90%">
              <div class="tag language">Backend</div>
            </div>
          </div>

          <div class="bar">
            <div class="fill" style="width: 80%">
              <div class="tag language">WebAPI</div>
            </div>
          </div>

          <div class="bar">
            <div class="fill" style="width: 80%">
              <div class="tag language">Relational databases</div>
            </div>
          </div>

          <div class="bar">
            <div class="fill" style="width: 80%">
              <div class="tag language">Python</div>
            </div>
          </div>

          <div class="bar">
            <div class="fill" style="width: 80%">
              <div class="tag language">Microcontrollers</div>
            </div>
          </div>

          <div class="bar">
            <div class="fill" style="width: 70%">
              <div class="tag language">Object Oriented Programming</div>
            </div>
          </div>

          <div class="bar">
            <div class="fill" style="width: 70%">
              <div class="tag language">Data Structures and Algorithms</div>
            </div>
          </div>

          <div class="bar">
            <div class="fill" style="width: 70%">
              <div class="tag language">Webscraping</div>
            </div>
          </div>
        </div> -->

        <div class="next">
          <div class="button">
            <div class="icon">
              <i
                @click="scrollToNextPage('projects')"
                class="fa fa-arrow-down"
              ></i>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section id="projects">
      <div class="projects" id="projects">
        <div class="title">Projects</div>
        <div>
          <div class="project-container">
            <div class="project">
              <div class="project-image">
                <img src="./assets/memory.png" alt="Memory" />
              </div>
              <div class="project-text">
                <div class="project-title">Memory</div>
                <div class="project-description">
                  A javascript memory game that was made for a school project.
                  During this project I learned how write responsive css and I
                  expended my knowledge of javascript.
                </div>
                <a class="github" href="https://github.com/leonbos1/memory"
                  >Github</a
                >
              </div>
            </div>

            <div class="project">
              <div class="project-image">
                <img
                  src="./assets/mobile-care-logo.png"
                  alt="Mobile care logo"
                />
              </div>
              <div class="project-text">
                <div class="project-title">MobilCare</div>
                <div class="project-description">
                  During this school project we made an application for an
                  elderly home. We used ESP32's to track elderly people using an
                  RFID tag. If something were to happen to the elderly person,
                  the ESP32 would send a message to the application. The
                  application would then send a message to the caretaker of the
                  elderly person. I learned Scrum, Python and SQL during this
                  project.
                </div>
                <a class="github" href="https://github.com/leonbos1/mobilecare"
                  >Github</a
                >
              </div>
            </div>

            <div class="project">
              <div class="project-image">
                <img
                  src="./assets/temperature.png"
                  alt="Room temperature webapp"
                />
              </div>
              <div class="project-text">
                <div class="project-title">Room temperature webapp</div>
                <div class="project-description">
                  A temperature application that I made using an ESP32,
                  Raspberry PI and Vue. During this project I learned about
                  webapi, Vue and SQL. Another big thing I learned during this
                  project is scalability. The project started out as a small
                  project but it grew into a big project. I learned how to scale
                  a project and how to keep it maintainable.
                </div>
                <a class="github" href="https://github.com/leonbos1/temperature"
                  >Github</a
                >
                <br />
                <a class="" href="http://leonbos.nl:8080/">Live demo</a>
              </div>
            </div>
          </div>
        </div>
        <div class="next">
          <div class="button">
            <div class="icon">
              <i
                @click="scrollToNextPage('contact')"
                class="fa fa-arrow-down"
              ></i>
            </div>
          </div>
        </div>
      </div>
    </section>
    <section id="contact">
      <div class="contact" id="contact">
        <div class="top">
          <div class="button">
            <div class="icon">
              <i @click="scrollToNextPage('home')" class="fa fa-arrow-up"></i>
            </div>
          </div>
        </div>

        <div class="title">Contact</div>

        <div class="wrapper">
          <div class="button email">
            <a href="mailto:bos.leon2001@gmail.com">
              <div class="icon">
                <i class="fa fa-envelope"></i>
              </div>
              <span>Email</span>
            </a>
          </div>

          <div class="button discord">
            <a href="https://discord.com/users/162641097460416512">
              <div class="icon">
                <i class="fab fa-discord"></i>
              </div>
              <span>Discord</span>
            </a>
          </div>

          <div class="button github">
            <a href="https://github.com/leonbos1">
              <div class="icon">
                <i class="fab fa-github"></i>
              </div>
              <span>Github</span>
            </a>
          </div>

          <div class="button linkedin">
            <a href="https://www.linkedin.com/in/leon-bos-0888a7215/">
              <div class="icon">
                <i class="fab fa-linkedin"></i>
              </div>
              <span>LinkedIn</span>
            </a>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: "App",
  components: {},

  data: function () {
    return {
      skills: {
        Backend: 90,
        WebAPI: 80,
        "Relational databases": 80,
        Python: 80,
        Microcontrollers: 80,
        "Object Oriented Programming": 70,
        "Data Structures and Algorithms": 70,
        Webscraping: 70,
      },
      visitors: 0,
      logs: [],
    };
  },

  mounted() {
    this.postLog();
    window.document.title = "Leon Bos";
  },

  methods: {
    scrollToNextPage(page) {
      if (page == "about") {
        for (const element in this.skills) {
          let el = document.getElementById(element);
          el.style.width = "0%";
          el.style.width = this.skills[element] + "%";
        }
      }
      document.getElementById(page).scrollIntoView({ behavior: "smooth" });
    },

    redirect(web) {
      window.location.href = web;
    },

    scrollToContact() {
      document.getElementById("contact").scrollIntoView({ behavior: "smooth" });
    },

    postLog() {
      fetch("http://leonbos.nl:5050/log", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
      });
    },
  },
};
</script>

<style lang="scss">
body {
  width: 100vw;
  height: 100vh;
  margin: 0;

  .container {
    height: 100%;
    width: 100%;

    section {
      display: flex;
      justify-content: center;
      align-items: center;
      width: 100vw;
      height: 100vh;
      scroll-snap-align: start;
      background-image: url("./assets/background.png");

      &:nth-of-type(1) {
        background-image: url("./assets/background3.png");
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-size: 100% 100%;
      }
      &:nth-of-type(2) {
        background-image: url("./assets/background2.png");
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-size: 100% 100%;
      }
      &:nth-of-type(3) {
        background-image: url("./assets/background4.png");
        //background-color: rgba(83, 32, 107, 0.555);
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-size: 100% 100%;
      }
      &:nth-of-type(4) {
        //background-color: rgba(0, 131, 33, 0.486);
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-size: 100% 100%;
      }
      &:nth-of-type(5) {
        //background-color: rgba(208, 212, 0, 0.411);
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-size: 100% 100%;
      }
    }

    section .home {
      .introduction {
        position: absolute;
        top: 40%;
        left: 50%;
        transform: translate(-50%, -50%);
        font-size: 3vw;
        color: white;
        font-family: "Montserrat", sans-serif;
        font-weight: 600;
        text-align: center;
      }
      button {
        background-color: transparent;
        border: 2px solid #e74c3c;
        border-radius: 0.6em;
        color: transparent;
        -webkit-align-self: center;
        -ms-flex-item-align: center;
        align-self: center;
        font-size: 1rem;
        line-height: 1;
        padding: 1.2em 2.8em;
        text-decoration: none;
        text-align: center;
        text-transform: uppercase;
        font-family: "Montserrat", sans-serif;
        font-weight: 400;
      }
      button:hover,
      button:focus {
        color: rgb(255, 255, 255);
        outline: 0;
      }

      button {
        color: #fff;
        box-shadow: 0 0 40px 40px #e74c3c inset, 0 0 0 0 #e74c3c;
        -webkit-transition: all 150ms ease-in-out;
        transition: all 150ms ease-in-out;
      }
      button:hover {
        box-shadow: 0 0 10px 0 #e74c3c inset, 0 0 10px 4px #e74c3c;
      }
      .nav {
        margin-top: 24vw;
        gap: 2vw;
        display: flex;
        justify-content: center;
        align-items: center;
      }

      @media (max-width: 600px) {
        .nav {
          margin-top: 35vh;
          height: 10vh;
          gap: 5vh;
          flex-direction: column;

          button {
            font-size: 2vh;
          }
        }
        .introduction {
          font-size: 6vw;
        }
      }
    }
  }
}

.name {
  color: red;
}

.about {
  width: 90%;
  position: absolute;
}

div .title {
  text-transform: uppercase;
  font-family: "Montserrat", sans-serif;
  font-weight: 700;
  font-size: 4vh;
  text-align: center;
}

div .about-text {
  padding: 5vh;
  font-family: "Montserrat", sans-serif;
  font-weight: 400;
  font-size: 1.5vw;
  max-width: 70vw;
  margin: auto;
  text-align: center;
}

@media screen and (max-width: 600px) {
  div .about-text {
    font-size: 3vw;
  }
}
.about-image {
  width: 100%;
  max-width: 17vw;
  height: auto;
  border-radius: 40%;
  //move to right
  margin-left: 60vw;
  margin-top: 30vh;
}

@media screen and (max-width: 600px) {
  .about-image {
    max-width: 23vw;
  }
}

.bar {
  position: relative;
  display: block;
  width: 40vw;
  height: 2.5vh;
  background: #eee;
  border-radius: 0.6em;
  margin: 1em 0;
  overflow: hidden;
  box-shadow: inset 0 0 0.5em rgba(0, 0, 0, 0.1);
}

.fill {
  position: relative;
  display: block;
  height: 100%;
  background: #b32a2a;
  border-radius: 0.6em;
  //animation everytime section scrolls into view
  animation: slideInFromLeft 1s ease-in-out;
}

@keyframes slideInFromLeft {
  0% {
    transform: translateX(-100%);
  }
  100% {
    transform: translateX(0);
  }
}

.tag {
  position: absolute;
  color: rgb(0, 0, 0);
  font-size: 100%;
  text-shadow: 0 0 0.5em rgba(0, 0, 0, 0.2);
  font-family: "Montserrat", sans-serif;
  top: 50%;
  font-size: 1vh;
  transform: translateY(-50%);
}

.contact-me {
  color: #ff0000;
}

.language {
  left: 1vw;
  font-size: 2vh;
}

@media screen and (max-width: 700px) {
  .language {
    font-size: 1.5vh;
  }
}

@media screen and (max-width: 500px) {
  .language {
    font-size: 1.2vh;
  }
}

@media screen and (max-width: 400px) {
  .language {
    font-size: 1vh;
  }
}

.percentage {
  right: 1vh;
}

.skill {
  align-items: center;
  width: 100%;
  height: 100%;
  // margin-left: 10%;
}

section .projects {
  //text needs to be readable
  color: rgb(255, 255, 255);

  img {
    margin-top: 50px;
    margin-left: 10%;
    width: 60%;
    height: 40%;
    border-radius: 5%;
    object-fit: cover;
    display: block;
    margin-left: auto;
    margin-right: auto;
    transition: 500ms;
  }

  .project-text {
    font-family: "Montserrat", sans-serif;
    font-weight: 400;
    font-size: 1.5vw;
    max-width: 70vw;
    margin: auto;
    text-align: center;
    margin-top: 50px;
  }

  .project {
    grid-gap: 10px;
    cursor: pointer;
    border: 1px solid black;
    border-radius: 50px;
    transition: all 0.6s;
    width: 25vw;
    height: 70vh;
  }

  .project:hover {
    transform: scale(1.2);
    background-color: rgba(0, 0, 0, 0.418);
  }

  img:hover {
    transform: scale(2.2);
    transition: 500ms;
  }

  .project-container {
    display: grid;
    grid-template-columns: auto auto auto;
    grid-template-rows: 1fr;
    grid-gap: 30px;
  }

  .project-title {
    font-family: "Montserrat", sans-serif;
    font-weight: 700;
    font-size: 2vw;
    text-align: center;
  }

  .project-description {
    font-family: "Montserrat", sans-serif;
    font-weight: 400;
    font-size: 1.2vw;
    text-align: center;
    padding: 10px;
  }
  @media screen and (max-width: 950px) {
    .project-description {
      font-size: 2.2vw;
    }
  }

  //make responsive
  @media screen and (max-width: 600px) {
    .project-container {
      grid-template-columns: auto;
    }

    .project {
      width: 70vw;
      height: 25vh;
    }

    img {
      margin-top: 5px;
      margin-left: 10%;
      width: 30%;
      height: 50%;
      border-radius: 5%;
      object-fit: cover;
      display: block;
      margin-left: auto;
      margin-right: auto;
    }

    .project-text {
      margin-top: 10px;
      width: 60%;
    }

    .project-description {
      font-size: 1vh;
    }
  }
}

section .blog {
  max-width: 80vw;
  font-size: 1vw;
}

section .contact {
  .top {
    top: 0;
    padding: 100px;
  }

  .contact-text {
    width: 90%;
    text-align: center;
  }
}

@import url("https://fonts.googleapis.com/css?family=Poppins:400,500,600,700&display=swap");

.wrapper .button {
  display: inline-block;
  height: 60px;
  width: 60px;
  margin: 0 5px;
  overflow: hidden;
  background: #fff;
  border-radius: 50px;
  cursor: pointer;
  box-shadow: 0px 10px 10px rgba(0, 0, 0, 0.1);
  transition: all 0.3s ease-out;
}
.wrapper .button:hover {
  width: 200px;
}
.wrapper .button .icon {
  display: inline-block;
  height: 60px;
  width: 60px;
  text-align: center;
  border-radius: 50px;
  box-sizing: border-box;
  line-height: 60px;
  transition: all 0.3s ease-out;
}

.email:hover .icon {
  background: #00ccff;
}

.discord:hover .icon {
  background: #4400ff;
}

.github:hover .icon {
  background: #000000;
}

.linkedin:hover .icon {
  background: rgb(0, 110, 255);
}
.wrapper .button .icon i {
  font-size: 25px;
  line-height: 60px;
  transition: all 0.3s ease-out;
  color: #000;
}
.wrapper .button:hover .icon i {
  color: #fff;
}
.wrapper .button span {
  font-size: 20px;
  font-weight: 500;
  line-height: 60px;
  margin-left: 10px;
  transition: all 0.3s ease-out;
}
.wrapper .button:nth-child(1) span {
  color: #00ccff;
}
.wrapper .button:nth-child(2) span {
  color: #4400ff;
}
.wrapper .button:nth-child(3) span {
  color: #000000;
}
.wrapper .button:nth-child(4) span {
  color: rgb(0, 110, 255);
}

div .wrapper {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 20vh;
  font-family: "Montserrat", sans-serif;
  font-weight: 700;
  position: relative;
}

div .next {
  text-align: center;
  margin-top: 20px;

  .button {
    display: inline-block;
    max-width: 20vw;
    max-height: 20vh;

    margin: 0 5px;
    overflow: hidden;
    background: #fff;
    border-radius: 50px;
    cursor: pointer;
    box-shadow: 0px 10px 10px rgba(0, 0, 0, 0.1);
    transition: all 0.3s ease-out;
  }
  .button .icon {
    display: inline-block;
    height: 60px;
    width: 60px;
    text-align: center;
    border-radius: 50px;
    box-sizing: border-box;
    line-height: 60px;
    transition: all 0.3s ease-out;
  }
  .button:nth-child(1):hover .icon {
    background: #6b6b6b;
  }
  .button .icon i {
    font-size: 25px;
    line-height: 60px;
    transition: all 0.3s ease-out;
  }
}

div .top {
  text-align: center;
  margin-top: 0px;

  .button {
    display: inline-block;
    max-width: 20vw;
    max-height: 20vh;
    margin: 0 5px;
    overflow: hidden;
    background: #fff;
    border-radius: 50px;
    cursor: pointer;
    box-shadow: 0px 10px 10px rgba(0, 0, 0, 0.1);
    transition: all 0.3s ease-out;
  }
  .button .icon {
    display: inline-block;
    height: 60px;
    width: 60px;
    text-align: center;
    border-radius: 50px;
    box-sizing: border-box;
    line-height: 60px;
    transition: all 0.3s ease-out;
  }
  .button:nth-child(1):hover .icon {
    background: #6b6b6b;
  }
  .button .icon i {
    font-size: 25px;
    line-height: 60px;
    transition: all 0.3s ease-out;
  }
}
</style>
