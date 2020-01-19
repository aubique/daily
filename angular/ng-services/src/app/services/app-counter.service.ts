import {Injectable} from "@angular/core";
import {LogService} from "./log.service";

// Singleton service
@Injectable({providedIn: 'root'})
export class AppCounterService {
  counter = 0;

  constructor(private logService: LogService) {
  }

  increase() {
    this.logService.log('increase counter...');
    this.counter++;
  }

  decrease() {
    this.logService.log('decrease counter...');
    this.counter--;
  }
}
