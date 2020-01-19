import {Injectable} from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class LogService {

  log(text: any): void {
    console.log(text);
  }
}
