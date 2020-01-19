import {Component} from '@angular/core';
import {AppCounterService} from "../services/app-counter.service";
import {LocalCounterService} from "../services/local-counter.service";

@Component({
  selector: 'app-counter',
  templateUrl: './counter.component.html',
  styleUrls: ['./counter.component.scss'],
  //copy of service
  providers: [LocalCounterService]
})
export class CounterComponent {

  constructor(
    private appCounterService: AppCounterService, //global instance
    private localCounterService: LocalCounterService //local copy
  ) {
  }

}
