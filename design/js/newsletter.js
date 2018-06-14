import { AjaxForm, FormHelper, MessageLevels } from './form';

export class NewsletterForm extends AjaxForm {

    handleSuccess(response) {
        this.form.addMessage('You have been subscribed', MessageLevels.SUCCESS);
        this.$form.get(0).reset();
    }

    handleError(response) {
        this.form.addMessage(
            'There was a problem adding you to the mailing list. Please try again.',
            MessageLevels.ERROR);
    }
}

NewsletterForm.fromElement = ($el) => {
    if ($el.length == 0) return null;
    return new NewsletterForm($el);
};
