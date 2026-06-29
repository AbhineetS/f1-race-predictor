export const circuitData = {
  "Spielberg": {
    name: "Austrian Grand Prix",
    circuit: "Red Bull Ring",
    location: "Spielberg, Austria",
    firstGp: "1970",
    fastestLap: "1:07.924 Oscar Piastri (2025)",
    length: "4.326km",
    laps: 71,
    distance: "307.018km",
    imageUrl: "https://media.formula1.com/image/upload/f_auto/q_auto/v1677244985/content/dam/fom-website/2018-redesign-assets/Circuit%20maps%2016x9/Austria_Circuit.png.transform/8col/image.png"
  },
  "Monza": {
    name: "Italian Grand Prix",
    circuit: "Autodromo Nazionale Monza",
    location: "Monza, Italy",
    firstGp: "1950",
    fastestLap: "1:21.046 Rubens Barrichello (2004)",
    length: "5.793km",
    laps: 53,
    distance: "306.720km",
    imageUrl: "https://media.formula1.com/image/upload/f_auto/q_auto/v1677244985/content/dam/fom-website/2018-redesign-assets/Circuit%20maps%2016x9/Italy_Circuit.png.transform/8col/image.png"
  },
  "Silverstone": {
    name: "British Grand Prix",
    circuit: "Silverstone Circuit",
    location: "Silverstone, UK",
    firstGp: "1950",
    fastestLap: "1:27.097 Max Verstappen (2020)",
    length: "5.891km",
    laps: 52,
    distance: "306.198km",
    imageUrl: "https://media.formula1.com/image/upload/f_auto/q_auto/v1677244985/content/dam/fom-website/2018-redesign-assets/Circuit%20maps%2016x9/Great_Britain_Circuit.png.transform/8col/image.png"
  },
  "Spa-Francorchamps": {
    name: "Belgian Grand Prix",
    circuit: "Circuit de Spa-Francorchamps",
    location: "Spa, Belgium",
    firstGp: "1950",
    fastestLap: "1:46.286 Valtteri Bottas (2018)",
    length: "7.004km",
    laps: 44,
    distance: "308.052km",
    imageUrl: "https://media.formula1.com/image/upload/f_auto/q_auto/v1677244985/content/dam/fom-website/2018-redesign-assets/Circuit%20maps%2016x9/Belgium_Circuit.png.transform/8col/image.png"
  },
  "Monte Carlo": {
    name: "Monaco Grand Prix",
    circuit: "Circuit de Monaco",
    location: "Monte Carlo, Monaco",
    firstGp: "1950",
    fastestLap: "1:12.909 Lewis Hamilton (2021)",
    length: "3.337km",
    laps: 78,
    distance: "260.286km",
    imageUrl: "https://media.formula1.com/image/upload/f_auto/q_auto/v1677244985/content/dam/fom-website/2018-redesign-assets/Circuit%20maps%2016x9/Monaco_Circuit.png.transform/8col/image.png"
  },
  "Suzuka": {
    name: "Japanese Grand Prix",
    circuit: "Suzuka International Racing Course",
    location: "Suzuka, Japan",
    firstGp: "1987",
    fastestLap: "1:30.983 Lewis Hamilton (2019)",
    length: "5.807km",
    laps: 53,
    distance: "307.471km",
    imageUrl: "https://media.formula1.com/image/upload/f_auto/q_auto/v1677244985/content/dam/fom-website/2018-redesign-assets/Circuit%20maps%2016x9/Japan_Circuit.png.transform/8col/image.png"
  }
};

export const getDefaultCircuit = () => ({
  name: "Grand Prix",
  circuit: "Unknown Circuit",
  location: "Unknown",
  firstGp: "N/A",
  fastestLap: "N/A",
  length: "0.000km",
  laps: 0,
  distance: "0.000km",
  imageUrl: ""
});
