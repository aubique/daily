import {Component} from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {

  title = 'Dynamic title';
  inputValue = '';

  constructor() {
  }

  onInput(event: KeyboardEvent) {
    this.inputValue = (event.target as HTMLInputElement).value;
  }

  onClick() {
  }

  onBlur(str: string) {
    this.inputValue = str;
  }
}
