import {Injectable} from '@angular/core';

@Injectable()
export class LocalCounterService {
  counter = 0;

  constructor() {
  }

  public increase() {
    this.counter++;
  }

  public decrease() {
    this.counter--;
  }
}
