{% load crispy_forms_tags %}
{% load static %}
<template>
  <div class="container" style="width: 500px">

<!-- Modal for Login Prompt -->
<div class="modal fade justify-content-center align-items-center
" id="loginModal" tabindex="-1" aria-labelledby="loginModalLabel" aria-hidden="true">
  <div class=“modal-dialog text-center“>
    <div class="modal-content rounded-4 shadow">
      <div class="modal-header p-5 pb-4 border-bottom-0">
        <h1 class="fw-bold mb-0 fs-2">Log in</h1>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body p-5 pt-0">
       <form method="post">
        {% csrf_token %}
        {{ form|crispy }}
        <button type="submit" class="form-control btn btn-primary mt-3">LOG IN</button>
      </form>
        <p class="mb-0">
        Need an account? <a href="{% url 'account_signup' %}">Register</a>.<br>
        Lost your password? <a href="{% url 'password_reset' %}">Reset it</a>.
      </p>

        </div>
      </div>
    </div>
  </div>

    <!-- Start Screen -->
    <div v-if="screen=='start'" class="container">
      <div class="row m-auto">
        <div class="col">
          <div class="row">
            <label for="word-length" class="form-label col">Word Length</label>
            <select id="word-length" class="form-select col" v-model="wordLength">
              <option v-for="key in Object.keys(anagrams)" :key="key" :value="key">
                {{ key }}
              </option>
            </select>
          </div>
        </div>
      </div>
      <div class="row m-auto">
        <ol>
          <li>Choose Word Length</li>
          <li>Press <strong>Play!</strong></li>
          <li>How many anagrams can you make in a minute?</li>
        </ol>
      </div>
      <button class="btn btn-primary w-100" @click="play">Play!</button>
    </div>

    <!-- Play Screen -->
    <div v-else-if="screen == 'play'" class="container">
      <div class="row">
        <div class="col d-flex justify-content-between">
          <span>Score: {{ score }}</span>
          <span>Time Left: {{ timeLeft }}</span>
        </div>
        <hr>
      </div>
      <div class="row">
        <output class="display-5 text-center">{{ currentWord }} ({{ guessesLeft }} left)</output>
      </div>
      <div class="row">
        <input class="form-control" v-model="userInput">
      </div>
      <div class="row text-center">
        <ol>
          <li v-for="guess in correctGuesses" :key="guess">{{ guess }}</li>
        </ol>
      </div>
    </div>

    <!-- End Screen -->
    <div v-else-if="screen == 'end'" class="container">
      <div class="row">
        <h4 class="display-4 text-center">Time's Up</h4>
      </div>
      <div class="row d-flex flex-col text-center">
        <p>You got</p>
        <div class="display-3">{{ score }}</div>
        <p>Anagrams</p>
      </div>
      <div class="row d-flex flex-col text-center">
        <button @click="play" class="btn btn-primary w-100 m-1">Play Again</button>
        <button @click="screen = 'start'" class="btn btn-secondary w-100 m-1">Back to Start Screen</button>
        <button onclick="window.location.href='/reviewing_anagram/'" class="btn btn-info w-100 m-1">Write AnagramHunt Review</button>
        <button onclick="window.location.href='/scoreboards/'" class="btn btn-light w-100 m-1">Check the Scoreboard</button>
      </div>
    </div>
  </div>
</template>

<style>
  div, label {
    padding: 0.2rem;
  }
</style>

<script type="module">
import anagrams from "@/helpers/anagrams";
import Axios from "axios";
Axios.defaults.withCredentials = true;
Axios.defaults.baseURL = "https://www.play2learn.app";

export default {
  name: 'AnagramGame',
  data() {
    return {
      userName: '',
      score: 0,
      timeLeft: 60,
      anagrams: anagrams,
      currentWord: "",
      anagramList: [],
      wordLength: 5,
      screen: "start",
      loggedIn: false,
      loggedInWarningDismissed: false,
      correctGuesses: [],
      userInput: "",
      interval: null,
      usedAnagramLists: [],
    };
  },
  methods: {
    getCsrfToken() {
      return document.querySelector('meta[name="csrf-token"]')?.getAttribute('content') || '';
    },
    async checkLogin() {
      try {
        const res = await Axios.get('/api/is-logged-in/', { withCredentials: true });
        this.loggedIn = res.data.logged_in;
      } catch (e) {
        this.loggedIn = false;
      }
    },
    async play() {
      await this.checkLogin();
      
      if (!this.loggedIn) {
        const modal = new bootstrap.Modal(document.getElementById('loginModal'));
        modal.show();
        return;
      }
      
      this.score = 0;
      this.timeLeft = 60;
      this.screen = "play";
      this.correctGuesses = [];
      this.usedAnagramLists = [];
      
      if (this.interval) clearInterval(this.interval);
      this.newAnagramList();
      
      this.interval = setInterval(() => {
        this.timeLeft--;
      }, 1000);
    },

    checkAnswer() {
      const input = this.userInput.toLowerCase();
      if (
        this.anagramList.includes(input) &&
        !this.correctGuesses.includes(input) &&
        this.currentWord !== input
      ) {
        this.correctGuesses.push(input);
        this.userInput = "";
        this.score++;

        if (this.correctGuesses.length === this.anagramList.length - 1) {
          this.newAnagramList();
        }
      }
    },
    newAnagramList() {
      const potentialAnagramLists = this.anagrams[this.wordLength] || [];

      const unusedLists = potentialAnagramLists.filter(
        list => !this.usedAnagramLists.some(used => used[0] === list[0])
      );

      if (unusedLists.length === 0) {
        this.screen = "end";
        return;
      }

      const chosenList = [...unusedLists[getRandomInteger(0, unusedLists.length)]];
      this.anagramList = chosenList;
      this.usedAnagramLists.push(chosenList);

      this.currentWord = this.anagramList[getRandomInteger(0, this.anagramList.length)];
      this.correctGuesses = [];
    },
    async recordScore() {
      try {
        await Axios.post('/api/record-score/anagramhunt/', {
          score: this.score,
          wordLength: this.wordLength,
          timeLeft: this.timeLeft
        }, {
          headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': this.getCsrfToken()
          },
          withCredentials: true
        });
        console.log("Score saved successfully");
      } catch (error) {
        console.error("Error saving score:", error);
      }
    }
  },
  watch: {
    userInput() {
      this.checkAnswer();
    },
    async timeLeft(newVal) {
      if (newVal === 0) {
        clearInterval(this.interval);
        await this.recordScore();
        this.timeLeft = 60;
        this.screen = "end";
      }
    }
  }
};
</script>