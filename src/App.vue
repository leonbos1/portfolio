<template>

<div class="container">

  <section id="home" class="home">
    <div id="home" class="home">
      <p class="introduction">Hello, my name is <span class="name">Leon Bos</span><br/> I'm a Software Engineering Student</p>
      <button class="btn third" @click="scrollToAbout">About Me</button>
    </div>
</section>

<section id="about">

  <div class="about" id="about">
    <div class="title">About</div>
    <img src="./assets/me.png" alt="Leon Bos" class="about-image">
    <div class="about-text">My name is Leon Bos and I'm a 20 year old Sofware Engineering student at the Hanzehogeschool Groningen.<br/>
      I am interested in many kinds of technologies and I am always looking for new challenges.<br/>
      Currently I am looking for a parttime job as a software developer to gain work experience while studying.<br/>
      If you want to know more about me, feel free to contact me.<br/>
      <br/>
      I have experience with the following technologies:<br/>
      <br/>
      <ul>
        <li>Java 3/5</li>
        <li>Python 4/5</li>
        <li>HTML 3/5</li>
        <li>CSS 2/5</li>
        <li>JavaScript 3/5</li>
        <li>Vue 3/5</li>
      </ul>
    </div>
    


    <div>
      
    </div>
  </div>
  

</section>

<section id="projects">

<div class="projects" id="projects">
  <div class="title">Projects</div>
</div>

</section>

<section id="blog">

<div class="blog" id="blog">
  <div class="title">Blog</div>
</div>

</section>

<section id="contact">

<div class="contact" id="contact">
  <div class="title">Contact</div>
</div>

</section>
</div>

</template>

<script>

export default {
  name: 'App',
  components: {
    
  },

  methods: {
    scrollToAbout() {
      document.getElementById('about').scrollIntoView({behavior: 'smooth'});
    }
  }
}
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

      &:nth-of-type(1) {
        background-image: url('./assets/background.png');
        background-repeat: no-repeat;
        background-attachment: fixed;; 
        background-size: 100% 100%;
      }
      &:nth-of-type(2) {
        background-color: #fff;
      }
      &:nth-of-type(3) {
        background-color: rgba(83, 32, 107, 0.555);
      }
    }
  }

}

.introduction {
  position: absolute;
  top: 40%;
  left: 50%;
  transform: translate(-50%, -50%);
  font-size: 3vw;
  color: white;
  font-family: 'Montserrat', sans-serif;
  font-weight: 600;
  text-align: center;
}
/*
@media screen and (max-width: 600px) {
  .introduction {
    font-size: 6vw;
  }
}
*/
.name {
  color: red;
}

.btn {
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
  font-family: 'Montserrat', sans-serif;
  font-weight: 700;
  margin-top: 40vh;
}
.btn:hover, .btn:focus {
  color: #fff;
  outline: 0;
}

.third {
  color: #fff;
  box-shadow: 0 0 40px 40px #e74c3c inset, 0 0 0 0 #e74c3c;
  -webkit-transition: all 150ms ease-in-out;
  transition: all 150ms ease-in-out;
}
.third:hover {
  box-shadow: 0 0 10px 0 #e74c3c inset, 0 0 10px 4px #e74c3c;
}

.about {
  width: 90%;
}

div .title {
  text-transform: uppercase;
  font-family: 'Montserrat', sans-serif;
  font-weight: 700;
  font-size: 3vw;
  text-align: center;
}

div .about-text {
  padding: 5vh;
  font-family: 'Montserrat', sans-serif;
  font-weight: 400;
  font-size: 1vw;
  max-width: 70vw;
  margin: auto;
  text-align: center;
}

div .project {
  background-color: rgba(255, 255, 255, 0.733);
}

.about-image {
  width: 10vh;
  height: auto;
  max-width: 100%;
  max-height: 100%;
  display: block;
  margin-left: auto;
  margin-right: auto;
  width: 30vh;
  border: 1px solid black;
  border-radius: 50%;
  float: left;
  margin-right: 5vh;
}

ul {
  position: relative;
  margin: 0;
  padding: 0;
  list-style: none;
  font-family: 'Montserrat', sans-serif;
  font-weight: 400;
  font-size: 1vw;
  max-width: 70vw;

  //center horizontally
  margin-left: auto;
  margin-right: auto;
  text-align: center;

}
</style>
