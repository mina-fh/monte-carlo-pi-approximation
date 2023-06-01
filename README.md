# Monte Carlo Pi Approximation

This repository contains Python code to approximate the value of Pi using the Monte Carlo method. The Monte Carlo method is a statistical technique that leverages random sampling to estimate numerical results.

## Code Description

The code in this repository generates random points within a square and checks if each point falls within a quarter circle inscribed within the square. By comparing the number of points within the circle to the total number of points generated, we can approximate the value of Pi.

The `inChk(x1, y1)` function checks whether a given point `(x1, y1)` falls within the inscribed circle. The main loop performs multiple iterations, increasing the sample size exponentially, and calculates the Pi approximation using the formula `(4 * Nin) / (Nin + Nout)`.

## Usage

1. Clone the repository:

```bash
git clone https://github.com/mina-fh/monte-carlo-pi-approximation.git

