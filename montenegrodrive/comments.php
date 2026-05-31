<?php
/**
 * Comments template
 *
 * @package MontenegroDrive
 */

if ( ! defined( 'ABSPATH' ) ) { exit; }

if ( post_password_required() ) {
    return;
}
?>
<div id="comments" class="comments-area mt-stack-lg">
    <?php if ( have_comments() ) : ?>
        <h2 class="font-h3 text-h3 text-primary mb-stack-md">
            <?php
            $comments_number = get_comments_number();
            printf(
                /* translators: %s: number of comments */
                esc_html( _n( '%s comment', '%s comments', $comments_number, 'montenegrodrive' ) ),
                esc_html( number_format_i18n( $comments_number ) )
            );
            ?>
        </h2>

        <ol class="comment-list list-none p-0 space-y-stack-md">
            <?php
            wp_list_comments(
                array(
                    'style'      => 'ol',
                    'short_ping' => true,
                )
            );
            ?>
        </ol>

        <?php the_comments_pagination(); ?>
    <?php endif; ?>

    <?php comment_form(); ?>
</div>
