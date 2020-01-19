import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'exMarks'
})
export class ExMarksPipe implements PipeTransform {

  transform(value: any, ...args: any[]): any {
    return null;
  }

}
