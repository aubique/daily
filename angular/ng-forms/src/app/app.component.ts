import {Component, OnInit} from '@angular/core'
import {FormControl, FormGroup} from "@angular/forms";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit {

  form: FormGroup;

  ngOnInit(): void {
    this.form = new FormGroup({
      email: new FormControl(''),
      password: new FormControl(null),
    });
  }

  submit() {
    console.log('Form submitted: ', this.form);
    // Spread {...} is similar to *list unpacking operator from Python
    const formData = {...this.form.value};
    console.log('Form data', formData);
  }
}
