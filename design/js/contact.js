import { AjaxForm, FormHelper, MessageLevels } from './form';

export class ContactForm extends AjaxForm {

    handleSuccess(response) {
        this.form.addMessage('Your message has been sent', MessageLevels.SUCCESS);
        this.$form.get(0).reset();
    }

    handleFormError(response) {
        return response.json()
        .then((json) => this.form.populateServerErrors(json));
    }

    handleError(response) {
        this.form.addMessage(
            'There was a problem adding you to the mailing list. Please try again.',
            MessageLevels.ERROR);
    }
}

ContactForm.fromElement = ($el) => {
    if ($el.length == 0) return null;
    return new ContactForm($el);
};
