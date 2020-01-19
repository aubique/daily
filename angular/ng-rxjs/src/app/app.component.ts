import {Component} from '@angular/core';
import {Subject, Subscription} from 'rxjs';

// import {} from 'rxjs/operators'

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {

  private sub: Subscription;
  private subjectStream: Subject<number> = new Subject<number>();
  private counter: number = 0;

  constructor() {
    // //Stream piping
    // const intervalStream$ = interval(1000);
    // this.sub = intervalStream$
    //   .pipe(
    //     filter(value => value % 2 === 0),
    //     map((value) => `Mapped value ${value}`),
    //     switchMap(() => interval(500))
    //   )
    //   .subscribe((value) => {
    //     console.log(value);
    //   })

    // // Create custom stream
    // const stream$ = new Observable(observer => {
    //   setTimeout(() => {
    //     observer.next(1);
    //   }, 1500);
    //
    //   // Complete executes itself if no error
    //   setTimeout(() => {
    //     observer.complete();
    //   }, 2100);
    //
    //   // Error terminates the stream
    //   setTimeout(() => {
    //     observer.error('Something went wrong')
    //   }, 2000);
    //
    //   setTimeout(() => {
    //     observer.next(2);
    //   }, 2500);
    // })
    //
    // this.sub = stream$
    //   .subscribe(
    //     value => console.log('Next: ', value),
    //     error => console.log('Error', error),
    //     () => console.log('Completed')
    //   );

    //Custom Subject extending Observable
    this.sub = this.subjectStream.subscribe(value => {
      console.log('Subscribe', value);
    });
  }

  next(): void {
    this.counter++;
    this.subjectStream.next(this.counter);
  }

  stop(): void {
    this.sub.unsubscribe();
  }
}
