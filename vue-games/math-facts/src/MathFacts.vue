<template>
  
  <div class="container" style="width: 500px">

<!-- Modal for Login Prompt -->
<div class="modal fade justify-content-center align-items-center" id="loginModal" tabindex="-1" aria-labelledby="loginModalLabel" aria-hidden="true">
  <div class="modal-dialog text-center">
    <div class="modal-content rounded-4 shadow">
      <div class="modal-header p-5 pb-4 border-bottom-0">
        <h1 class="fw-bold mb-0 fs-2">Log in</h1>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body p-5 pt-0">
        <form method="post" action="/accounts/login/">
          <div class="form-floating mb-3">
            <input type="email" class="form-control rounded-3" id="loginEmail" name="login" placeholder="name@example.com">
            <label for="loginEmail">Email address</label>
          </div>
          <div class="form-floating mb-3">
            <input type="password" class="form-control rounded-3" id="loginPassword" name="password" placeholder="Password">
            <label for="loginPassword">Password</label>
          </div>
          <button type="submit" class="w-100 mb-2 btn btn-lg rounded-3 btn-primary">Log in</button>
        </form>

        <div class="text-center mt-3">
          <small class="text-muted">Don't have an account?</small>
          <a href="/accounts/signup/" class="btn btn-outline-secondary w-100 mt-2 rounded-3">Sign up</a>
        </div>
      </div>
    </div>
  </div>
</div>

    <!-- Start Screen -->
    <div v-if="screen=='start'" class="container">
      <div class="row">
        <div class="col">
          <div class="row">
            <label for="operation" class="form-label col-3">Operation</label>
            <select id="operation" class="form-select col" v-model="operation">
              <option v-for="symbol, operation in operations" :key="operation" :value="symbol">
                {{ operation }}
              </option>
            </select>
          </div>
          <div class="row">
            <label for="max-number" class="form-label col-3 mathfacts-label">Max Number</label>
            <input id="max-number" class="form-control col" type="number" min="1" max="100" v-model="maxNumber">
          </div>
        </div>
      </div>
      <div class="row m-auto">
        <ol>
          <li>Choose Operation and Max Number</li>
          <li>Press <strong>Play!</strong></li>
          <li>How many questions can you get in a minute?</li>
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
        <output class="display-5 text-center">{{ number1 }} {{ operation }} {{ number2 }} = </output>
      </div>
      <div class="row">
        <input class="form-control m-auto" v-model="userInput" style="width: 200px">
      </div>
      <div class="row m-auto" style="width: 300px">
        <div class="row gx-2 mb-2">
          <div class="col-4">
            <button @click="userInput += '1'" class="btn btn-primary w-100">1</button>
          </div>
          <div class="col-4">
            <button @click="userInput += '2'" class="btn btn-primary w-100">2</button>
          </div>
          <div class="col-4">
            <button @click="userInput += '3'" class="btn btn-primary w-100">3</button>
          </div>
        </div>
        <div class="row gx-2 mb-2">
          <div class="col-4">
            <button @click="userInput += '4'" class="btn btn-primary w-100">4</button>
          </div>
          <div class="col-4">
            <button @click="userInput += '5'" class="btn btn-primary w-100">5</button>
          </div>
          <div class="col-4">
            <button @click="userInput += '6'" class="btn btn-primary w-100">6</button>
          </div>
        </div>
        <div class="row gx-2 mb-2">
          <div class="col-4">
            <button @click="userInput += '7'" class="btn btn-primary w-100">7</button>
          </div>
          <div class="col-4">
            <button @click="userInput += '8'" class="btn btn-primary w-100">8</button>
          </div>
          <div class="col-4">
            <button @click="userInput += '9'" class="btn btn-primary w-100">9</button>
          </div>
        </div>
        <div class="row gx-1">
          <div class="col-4">
            <button @click="userInput += '0'" class="btn btn-primary w-100">0</button>
          </div>
          <div class="col-8">
            <button @click="userInput = ''" class="btn btn-primary w-100">Clear</button>
          </div>
        </div>
      </div>
    </div>
    <!-- End Screen -->
    <div v-else-if="screen == 'end'" class="container">
      <div class="row">
        <h4 class="display-4 text-center">Time's Up</h4>
      </div>
      <div class="row d-flex flex-col text-center">
        <p>You answered</p>
        <div class="display-3">{{ score }}</div>
        <p>questions</p>
      </div>
      <div class="row d-flex flex-col text-center">
        <button @click="play" class="btn btn-primary w-100 m-1">Play Again</button>
        <button @click="screen = 'start'" class="btn btn-secondary w-100 m-1">Back to Start Screen</button>
        <button onclick="window.location.href='/reviewing_math/'" class="btn btn-info w-100 m-1">Write MathFacts Review</button>
        <button onclick="window.location.href='/scoreboards/my-scores/'" class="btn btn-success w-100 m-1">Check your Scoreboard</button>
        <button onclick="window.location.href='/scoreboards/'" class="btn btn-light w-100 m-1">Check the Leaderboard</button>
      </div>
    </div>
  </div>
</template>

<script type="module">
import { getRandomInteger } from './helpers/helpers';
import Axios from 'axios';

Axios.defaults.baseURL = "https://www.play2learn.app";
Axios.defaults.withCredentials = true;

export default {
  name: 'MathGame',
  data() {
    return {
      score: 0,
      screen: "start",
      loggedIn: false,
      loggedInWarningDismissed: false,
      maxNumber: 30,
      operation: "+",
      operations: {
        "Addition": "+",
        "Subtraction": "-",
        "Multiplication": "x",
        "Division": "/"
      },
      number1: 0,
      number2: 0,
      userInput: "",
      interval: null,
      timeLeft: 60,
    };
  },
  mounted() {
    this.checkLogin();
  },
  methods: {
    getCsrfToken() {
      const match = document.cookie.match(/csrftoken=([^;]+)/);
      return match ? match[1] : '';
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
        const modalEl = document.getElementById('loginModal');
        if (modalEl) {
          const modal = new bootstrap.Modal(modalEl);
          modal.show();
        }
        this.loggedInWarningDismissed = false;
        return;
      }

      this.screen = "play";
      this.getNewQuestion();

      if (this.interval) clearInterval(this.interval);

      this.interval = setInterval(() => {
        this.timeLeft--;
      }, 1000);
    },

    getNewQuestion() {
      let num1 = getRandomInteger(0, this.maxNumber + 1);
      let num2 = getRandomInteger(0, this.maxNumber + 1);
      if (this.operation === "-") {
        this.number1 = Math.max(num1, num2);
        this.number2 = Math.min(num1, num2);
      } else if (this.operation === "/") {
        this.number1 = num1 * num2;
        this.number2 = num2;
      } else {
        this.number1 = num1;
        this.number2 = num2;
      }
    },

    async recordScore() {
      const userData = {
        score: this.score,
        operation: this.operation,
        maxNumber: this.maxNumber,
        timeLeft: this.timeLeft
      };
      try {
        await Axios.post('/api/record-score/mathfacts/', userData, {
          headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': this.getCsrfToken()
          }
        });
        console.log("Score saved successfully");
      } catch (error) {
        console.error("Error saving score:", error);
      }
    }
  },
  computed: {
    correctAnswer() {
      if (!this.userInput.trim()) return false;
      const input = parseInt(this.userInput);
      if (this.operation === "+") return input === this.number1 + this.number2;
      if (this.operation === "-") return input === this.number1 - this.number2;
      if (this.operation === "x") return input === this.number1 * this.number2;
      if (this.operation === "/") return input === this.number1 / this.number2;
      return false;
    }
  },
  watch: {
    userInput() {
      if (this.correctAnswer) {
        this.score++;
        this.getNewQuestion();
        this.userInput = "";
      }
    },

    async timeLeft(newVal) {
      if (newVal === 0) {
        clearInterval(this.interval);
        this.timeLeft = 60;
        await this.recordScore();
        this.screen = "end";
      }
    }
  }
};
</script>