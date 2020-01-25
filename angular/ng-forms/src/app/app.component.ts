import {Component, OnInit} from '@angular/core'
import {FormArray, FormControl, FormGroup, Validators} from "@angular/forms";
import {MyValidators} from "./my.validators";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit {
  form: FormGroup;

  ngOnInit(): void {
    this.form = new FormGroup({
      email: new FormControl('', [
        Validators.email,
        Validators.required,
        MyValidators.restrictedEmails
      ], [MyValidators.uniqEmail]),
      password: new FormControl(null,
        [
          Validators.required,
          Validators.minLength(6)
        ]),
      address: new FormGroup({
        // Options for this select are declared in template
        country: new FormControl('ru'),
        // dict of cities is init'd onButtonClick by setCapital()
        city: new FormControl('', Validators.required)
      }),
      // Controls are init'd dynamically onButtonClick by addSkill()
      skills: new FormArray([])
    })
  }

  submit() {
    if (this.form.valid) {
      console.log('Form submitted: ', this.form);
      // Spread {...} is similar to *list unpacking operator from Python
      const formData = {...this.form.value};

      console.log('Form data', formData);
      // Clean the whole form up
      this.form.reset();
    }
  }

  setCapital() {
    const cityMap = {
      ru: 'Moscow',
      ua: 'Kyiv',
      by: 'Minsk'
    };

    const cityKey = this.form.get('address').get('country').value;
    const city = cityMap[cityKey];
    // Patch formGroup.formControl by (address.city:city)
    this.form.patchValue({address: {city}});
  }

  // Push one FormControl more to FormArray
  addSkill(): void {
    const control = new FormControl('', Validators.required);
    // (<FormArray>this.form.get('skills')).push(control);
    (this.form.get('skills') as FormArray).push(control);
  }
}
