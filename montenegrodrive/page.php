<?php
/**
 * Default page template
 *
 * When a page is built with Elementor, the_content() renders the Elementor
 * output. We give Elementor the entire content area edge-to-edge by setting
 * the wrapper to take full width.
 *
 * For pixel-perfect control over a single page, use Elementor's "Elementor Canvas"
 * page template (no header / no footer) instead — it's available in the page editor's
 * Page Attributes → Template dropdown once Elementor is active.
 *
 * @package MontenegroDrive
 */

if ( ! defined( 'ABSPATH' ) ) { exit; }

get_header();
?>

<?php while ( have_posts() ) : the_post(); ?>

    <article id="post-<?php the_ID(); ?>" <?php post_class( 'page-content' ); ?>>
        <?php the_content(); ?>

        <?php
        wp_link_pages(
            array(
                'before' => '<div class="page-links px-gutter max-w-container-max mx-auto py-stack-md">' . esc_html__( 'Pages:', 'montenegrodrive' ),
                'after'  => '</div>',
            )
        );
        ?>
    </article>

    <?php if ( comments_open() || get_comments_number() ) : ?>
        <div class="max-w-container-max mx-auto px-gutter py-stack-lg">
            <?php comments_template(); ?>
        </div>
    <?php endif; ?>

<?php endwhile; ?>

<?php get_footer();
