<template>
  <div class="container" style="width: 500px">
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
        <div class="row gx-1">
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
        <div class="row gx-1">
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
        <div class="row gx-1">
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

<script type="text/javascript">
const csrfToken = "{{ csrf_token }}"
import { getRandomInteger } from '@/helpers/helpers';
import Axios from 'axios';

export default {
  name: 'MathGame',
  data() {
    return {
      score: 0,
      screen: "start",
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
    }
  },
  methods: {
    play() {
      this.screen = "play";
      this.getNewQuestion();
      this.interval = setInterval(() => {
        this.timeLeft--;
      }, 1000)
    },
    getNewQuestion() {
      let num1 = getRandomInteger(0, this.maxNumber + 1);
      let num2 = getRandomInteger(0, this.maxNumber + 1);
      if (this.operation == "-") {
        this.number1 = Math.max(num1, num2);
        this.number2 = Math.min(num1, num2);
      }
      else if (this.operation == "/") {
        this.number1 = num1 * num2;
        this.number2 = num2;
      }
      else {
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
        const response = await Axios.post('/games/api/record-score/mathfacts/', userData, {
          headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken
          },
          withCredentials: true
        });
        console.log("Saved successfully", response.data);
      } catch (error) {
        console.error("Error saving", error);
      }
    }
  },
  computed: {
    correctAnswer() {
      if (this.userInput.trim() == "") {
        return false;
      }

      const input = parseInt(this.userInput);
      if (this.operation == "+") {
        return input === this.number1 + this.number2;
      }

      if (this.operation == "-") {
        return input === this.number1 - this.number2;
      }

      if (this.operation == "x") {
        return input === this.number1 * this.number2;
      }

      if (this.operation == "/") {
        return input === this.number1 / this.number2;
      }

      return false;
    },
  },
  watch: {
    userInput() {
      if (this.correctAnswer) {
        this.score++; 
        this.getNewQuestion();
        this.userInput = "";
      }
    },
    async timeLeft(newTime) {
      if (newTime === 0) {
        clearInterval(this.interval);
        this.timeLeft = 60;
        await this.recordScore();
        this.screen = "end";
        console.log("Time's up! Your score is added");
      }
    }
  }
}
</script>