document.addEventListener('DOMContentLoaded', function() {
    document.addEventListener('mousedown', function(e) {
        if (e.target.tagName === 'OPTION' && e.target.parentElement.hasAttribute('multiple')) {
            e.preventDefault();
            
            const select = e.target.parentElement;
            const scroll = select.scrollTop;
            
            // Toggle selection
            e.target.selected = !e.target.selected;
            
            // Trigger change event to notify forms
            select.dispatchEvent(new Event('change', { bubbles: true }));
            
            // Keep focus and restore scroll instantly
            select.focus();
            setTimeout(() => {
                select.scrollTop = scroll;
            }, 0);
        }
    });
});
