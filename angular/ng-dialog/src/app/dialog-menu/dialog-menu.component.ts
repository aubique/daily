import {Component, Inject, OnInit} from '@angular/core';
import {FormBuilder, FormGroup, Validators} from '@angular/forms';
import {MAT_DIALOG_DATA, MatDialogRef} from '@angular/material/dialog';

@Component({
  selector: 'app-dialog-menu',
  templateUrl: './dialog-menu.component.html',
  styleUrls: ['./dialog-menu.component.scss']
})
export class DialogMenuComponent implements OnInit {

  form: FormGroup;
  identification: number;

  constructor(
    private fb: FormBuilder,
    private dialogRef: MatDialogRef<DialogMenuComponent>,
    @Inject(MAT_DIALOG_DATA) {id, title}: any
  ) {
    this.identification = id;
    this.form = this.fb.group({
      'id': [id, [Validators.required, Validators.pattern('^[0-9]+$')]],
      'title': [title, Validators.required],
    });
  }

  ngOnInit(): void {
  }

  onClose(): void {
    this.dialogRef.close(this.form.value);
  }
}
